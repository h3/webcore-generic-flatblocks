from django.db import models
from django.utils.translation import ugettext_lazy as _

class Title(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)

    def __unicode__(self):
        return "(TitleBlock) %s" % self.title

class Text(models.Model):
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(TextBlock) %s..." % self.text[:20]

class TranslatedImage(models.Model):
    image_en = models.ImageField(_('image (en)'), upload_to='gblocks/', blank=True)
    image_fr = models.ImageField(_('image (fr)'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TranslatedImageBlock) %s" % self.image_fr

class TranslatedImageAndLink(models.Model):
    image_en = models.ImageField(_('image (en)'), upload_to='gblocks/', blank=True)
    image_fr = models.ImageField(_('image (fr)'), upload_to='gblocks/', blank=True)
    link  = models.CharField(_('link'), max_length=255, blank=True)

    def __unicode__(self):
        return "(TranslatedImageLinkBlock) %s" % self.image_fr

class Image(models.Model):
    image = models.ImageField(_('image'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(ImageBlock) %s" % self.image

class ImageAndLink(models.Model):
    image = models.ImageField(_('image'), upload_to='gblocks/', blank=True)
    link  = models.CharField(_('link'), max_length=255, blank=True)

    def __unicode__(self):
        return "(ImageLinkBlock) %s" % self.image

class TitleAndFile(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    image = models.FileField(_('file'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TitleAndFileBlock) %s" % self.title

class TranslatedTitleAndFile(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    file_fr = models.FileField(_('file (fr)'), upload_to='gblocks/', blank=True)
    file_en = models.FileField(_('file (en)'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TranslatedTitleAndFileBlock) %s" % self.title

class TitleTextAndFile(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)
    file = models.FileField(_('file'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TitleTextAndFileBlock) %s" % self.title

class TitleAndText(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(TitleAndTextBlock) %s" % self.title

class TitleTextAndImage(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)
    image = models.ImageField(_('image'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TitleTextAndImageBlock) %s" % self.title

class TranslatedTitleTextAndImage(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)
    image_en = models.ImageField(_('image (en)'), upload_to='gblocks/', blank=True)
    image_fr = models.ImageField(_('image (fr)'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TranslatedTitleTextAndImageBlock) %s" % self.title
