from django.contrib import admin

# Register your models here.
from .models import Produit, Tag, Categorie, Image

class ImageInline(admin.StackedInline):
    model = Image

class ProduitAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    #raw_id_fields = ("Tags","Categories")

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Tag)
admin.site.register(Categorie)