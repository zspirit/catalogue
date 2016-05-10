from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
#from django.http import Http404

from .models import Produit, Tag, Categorie

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'produit/index.html'
    context_object_name = 'latest_produits_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Produit.objects.all().order_by('-title')[:5]

class DetailView(generic.DetailView):
    model = Produit
    template_name = 'produit/detail.html'
    context_object_name = 'product'