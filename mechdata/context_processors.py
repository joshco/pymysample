from django.conf import settings # import the settings file

def my_tags(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'OSDI_BROWSER': settings.OSDI_BROWSER,
            'NAV_TITLE': settings.NAV_TITLE }
