# -*- coding: utf-8 -*-

"""

    threatmetrix.tests.threatmetrix
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    unit tests testing the template tag
    
"""
from django.template.base import Template
from django.template.context import Context
from django.test.testcases import TestCase

class WhenRenderingThreatMetrixTemplateTags(TestCase):

    expected_out = u'\n\n<div id="tmx" style="display:none;">\n    <p style="background:url(https://h.online-metrix.net/fp/clear.png?org_id=test_org_id&amp;session_id=request_num&amp;session2=99a0008e49be4dc88b7c083273cfad9a&amp;m=1)"></p>\n\n    <img src="https://h.online-metrix.net/fp/clear.png?org_id=test_org_id&amp;session_id=request_num&amp;m=2" alt="" />\n    <script src="https://h.online-metrix.net/fp/check.js?org_id=test_org_id&amp;session_id=request_num" type="text/javascript"></script>\n    <object type="application/x-shockwave-flash" data="https://h.online-metrix.net/fp/fp.swf?org_id=test_org_id&amp;session_id=request_num" width="1" height="1" id="thm_fp">\n        <param name="movie" value="https://h.online-metrix.net/fp/fp.swf?org_id=test_org_id&amp;session_id=request_num" />\n    </object>\n</div>\n\n'

    @property
    def tm_enabled(self):
        from ..templatetags import threatmetrix
        setattr(threatmetrix, 'THREATMETRIX_JS_ENABLED', True)
        return threatmetrix.THREATMETRIX_JS_ENABLED

    def setUp(self):

        self.tm_enabled

        self.rendered = self.render_template(
            '{% load threatmetrix %}'
            '{% threat_metrix_tags "request_num" %}'
        )

    def test_rendering_as_expected(self):
        self.assertEqual(self.rendered, self.expected_out )

    def render_template(self, template_string, context_params=None):
        t = Template(template_string)
        c = Context(context_params)
        return t.render(c)

class WithTMDisabled(WhenRenderingThreatMetrixTemplateTags):

    expected_out = u'\n<!-- Skipping threatmetrix for this request -->\n'

    @property
    def tm_enabled(self):
        from ..templatetags import threatmetrix
        setattr(threatmetrix, 'THREATMETRIX_JS_ENABLED', False)
        return threatmetrix.THREATMETRIX_JS_ENABLED

    def test_rendering_as_expected(self):
        self.assertEqual(self.rendered, self.expected_out )