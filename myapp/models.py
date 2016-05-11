from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Postable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Post(Postable):
    """docstring for Produit"""
    title = models.CharField(max_length = 255)
    slug = models.CharField(blank=True, null=True, max_length = 255)
    description = models.TextField(blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)
    poids = models.FloatField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
