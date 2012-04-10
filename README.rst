===================
django-threatmetrix
===================

django-threatmetrix makes it easy to apply the  in your django application. You just need to do the following.

Installation
============
1. Install django-threatmetrix using easy_setup or pip::

    pip install django-threatmetrix

2. add like_button to your INSTALLED_APPS in your django settings file::

    INSTALLED_APPS = (
        # all
        # other 
        # apps
        'threatmetrix',
    )

3. Add "THREATMETRIX_ORG_ID" setting to your django settings file with your threatmetrix org id.

    in settings.py::

        THREATMETRIX_ORG_ID = "Your org id"
        THREATMETRIX_URL = "https://h.online-metrix.net" # Optional
        THREATMETRIX_JS_ENABLED = True  # Optional

4. Add the template tag code into your base template before the body tag.

    Where you need the threatmetrix tag::

    {% load threatmetrix %}

    Where ever you want your threatmetrix tag use:

    {% threat_metrix_tags object.value %}
