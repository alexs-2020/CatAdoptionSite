from django.shortcuts import render
from catList.models import Cat  # Importing from the 'cats' app

# Create your views here.
def home(request):
    cats = Cat.objects.all()  # Retrieve all cats with images
    return render(request, 'home.html', {'cats': cats})

def about(request):
    return render(request, "nuestraFamilia.html")

def history(request):
    return render(request, "historia.html")
