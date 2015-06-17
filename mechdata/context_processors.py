from django.conf import settings # import the settings file

def osdi_browser(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'OSDI_BROWSER': settings.OSDI_BROWSER}
