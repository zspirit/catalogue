from django.contrib import admin

# Register your models here.
from .models import Produit, Tag, Categorie, Image

admin.site.register(Produit)
admin.site.register(Tag)
admin.site.register(Categorie)
admin.site.register(Image)