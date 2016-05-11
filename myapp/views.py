from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def handel_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            obj = Post()
            obj.title = request.POST['title']
            obj.description = request.POST['description']
            obj.prix = request.POST['prix']
            obj.save()
            return HttpResponse("Formulaire Valide.")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'form.html', {'form': form})