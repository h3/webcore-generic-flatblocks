from django.conf import settings
from django.contrib import admin
from django_generic_flatblocks.contrib.gblocks.models import *


if 'grappellifit' in settings.INSTALLED_APPS and 'modeltranslation' in settings.INSTALLED_APPS:
    from grappellifit.admin import TranslationAdmin
    
    admin.site.register(Title, TranslationAdmin)
    admin.site.register(Text, TranslationAdmin)
    admin.site.register(Image)
    admin.site.register(ImageAndLink, TranslationAdmin)
    admin.site.register(TitleAndFile, TranslationAdmin)
    admin.site.register(TitleTextAndFile, TranslationAdmin)
    admin.site.register(TitleAndText, TranslationAdmin)
    admin.site.register(TitleTextAndImage, TranslationAdmin)

else:
    admin.site.register(Title)
    admin.site.register(Text)
    admin.site.register(Image)
    admin.site.register(ImageAndLink)
    admin.site.register(TitleAndFile)
    admin.site.register(TitleTextAndFile)
    admin.site.register(TitleAndText)
    admin.site.register(TitleTextAndImage)

