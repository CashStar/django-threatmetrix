import logging
from hashlib import md5

from django.template import Library
from django.conf import settings

register = Library()
log = logging.getLogger(__name__)

THREATMETRIX_JS_ENABLED = getattr(settings, 'THREATMETRIX_JS_ENABLED', False)
THREATMETRIX_URL = getattr(settings, 'THREATMETRIX_URL',
    'https://h.online-metrix.net')
THREATMETRIX_ORG_ID = getattr(settings, 'THREATMETRIX_ORG_ID', None)


@register.inclusion_tag('threatmetrix/threatmetrix_js_tag.html')
def threat_metrix_tags(token):
    """ Custom threatmetrix template tag

        :param token: tag passed to threatmetrix
    """
    if not THREATMETRIX_JS_ENABLED:
        return dict(THREATMETRIX_JS_ENABLED=False)

    if not THREATMETRIX_ORG_ID:
        log.warning("threat_metrix_tag is incorrectly configured, you must "
                    "supply an THREATMETRIX_ORG_ID")
        return dict(THREATMETRIX_JS_ENABLED=False)

    return dict(
        THREATMETRIX_JS_ENABLED=True,
        THREATMETRIX_URL=THREATMETRIX_URL,
        THREATMETRIX_ORG_ID=THREATMETRIX_ORG_ID,
        THREATMETRIX_SESSION_ID=token,
        THREATMETRIX_SESSION_ID_2=md5(str(token)).hexdigest(),
    )
