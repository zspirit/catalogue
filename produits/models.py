from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Produit(models.Model):
    """docstring for Produit"""
    title = models.CharField(max_length = 255)
    description = models.TextField()
    prix = models.FloatField()
    poids = models.FloatField()
    tags = models.ManyToManyField('Tag')
    categories = models.ManyToManyField('Categorie')
    visible = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ('title',)

class Tag(models.Model):
    """docstring for Tags"""
    tag = models.CharField(max_length = 255)
    def __unicode__(self):
        return self.tag

class Categorie(models.Model):
    """docstring for Categories"""
    categorie = models.CharField(max_length = 255)
    def __unicode__(self):
        return "%s" % (self.categorie)
    class Meta:
        ordering = ('categorie',)

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "produits/static/uploads/%s-%s" % (slug, filename) 

class Image(models.Model):
    post = models.ForeignKey(Produit, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
    def __unicode__(self):
        return "Image du produit : %s" % (self.post.title) 