# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from django_generic_flatblocks.contrib.gblocks.models import *


class TitleOptions(TranslationOptions):
    fields = ('title',)
translator.register(Title, TitleOptions)


class TextOptions(TranslationOptions):
    fields = ('text',)
translator.register(Text, TextOptions)


class ImageAndLinkOptions(TranslationOptions):
    fields = ('link',)
translator.register(ImageAndLink, ImageAndLinkOptions)


class TitleAndFileOptions(TranslationOptions):
    fields = ('title',)
translator.register(TitleAndFile, TitleAndFileOptions)


class TitleTextAndFileOptions(TranslationOptions):
    fields = ('title',)
translator.register(TitleTextAndFile, TitleTextAndFileOptions)


class TitleAndTextOptions(TranslationOptions):
    fields = ('title', 'text',)
translator.register(TitleAndText, TitleAndTextOptions)


class TitleTextAndImageOptions(TranslationOptions):
    fields = ('title', 'text',)
translator.register(TitleTextAndImage, TitleTextAndImageOptions)
