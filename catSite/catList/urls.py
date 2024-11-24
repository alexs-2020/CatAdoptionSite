from django.urls import path
from . import views

urlpatterns = [
    path('cats/', views.catList, name="catList"),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat_detail'),
    path('machos/', views.machos, name='machos'),
    path('hembras/', views.hembras, name='hembras'),

]