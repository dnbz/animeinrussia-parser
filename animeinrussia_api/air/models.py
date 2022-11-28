from django.db import models

class Show(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    sent_at = models.DateTimeField(default=None, blank=True, null=True)

    source_url = models.CharField('URL of the show', max_length=255, default=None)
    description = models.TextField(default=None, blank=True, null=True)
    title_orig = models.CharField('Original title', max_length=255, default=None, blank=True, null=True)
    title_ru = models.CharField('Translated title', max_length=255, default=None, blank=True, null=True)
    image_url = models.CharField('Image URL', max_length=255, default=None, blank=True, null=True)
    pub_date = models.DateTimeField('Published date', default=None, blank=True, null=True)

# Create your models here.
