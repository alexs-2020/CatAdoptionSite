from django.shortcuts import render, get_object_or_404

from catList.models import Cat
#
# def catList(request):
#     cats = Cat.objects.all()
#     selected_cat = None
#
#     # Check if a specific cat is selected
#     if 'selected_cat' in request.GET:
#         selected_cat_id = request.GET.get('selected_cat')
#         selected_cat = get_object_or_404(Cat, id=selected_cat_id)
#
#     return render(request, 'catList.html', {
#         'cats': cats,
#         'selected_cat': selected_cat,
#     })
#
# def machos(request):
#     cats = Cat.objects.filter(sexo='macho')
#     print(cats)  # Log to console
#     return render(request, 'catList.html', {'cats': cats})
#
# def hembras(request):
#     cats = Cat.objects.filter(sexo='hembra')
#     return render(request, 'catList.html', {'cats': cats})


from django.shortcuts import render, get_object_or_404
from .models import Cat

def catList(request):
    cats = Cat.objects.all()
    selected_cat = None

    # Check if a specific cat is selected
    if 'selected_cat' in request.GET:
        selected_cat_id = request.GET.get('selected_cat')
        selected_cat = get_object_or_404(Cat, id=selected_cat_id)

    return render(request, 'catList.html', {
        'cats': cats,
        'selected_cat': selected_cat,
    })

def machos(request):
    cats = Cat.objects.filter(sexo='macho')
    selected_cat = None

    # Check if a specific cat is selected
    if 'selected_cat' in request.GET:
        selected_cat_id = request.GET.get('selected_cat')
        selected_cat = get_object_or_404(Cat, id=selected_cat_id)

    return render(request, 'catList.html', {
        'cats': cats,
        'selected_cat': selected_cat,
    })

def hembras(request):
    cats = Cat.objects.filter(sexo='hembra')
    selected_cat = None

    # Check if a specific cat is selected
    if 'selected_cat' in request.GET:
        selected_cat_id = request.GET.get('selected_cat')
        selected_cat = get_object_or_404(Cat, id=selected_cat_id)

    return render(request, 'catList.html', {
        'cats': cats,
        'selected_cat': selected_cat,
    })