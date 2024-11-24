from django.shortcuts import render, get_object_or_404

from catList.models import Cat


# Create your views here.
def catList(request):
    cats = Cat.objects.all()  # Query to retrieve all Cat objects
    print(cats)  # Log to console
    return render(request, 'catList.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'catDetails.html', {'cat': cat})

def machos(request):
    cats = Cat.objects.filter(sexo='macho')
    print(cats)  # Log to console
    return render(request, 'catList.html', {'cats': cats})

def hembras(request):
    cats = Cat.objects.filter(sexo='hembra')
    return render(request, 'catList.html', {'cats': cats})