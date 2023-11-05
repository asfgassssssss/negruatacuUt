from django.contrib import admin
from django.urls import path

from XJIe6.views import index, archive, SFASFGAS, sdghsdfh, kub, animales
from . import views
urlpatterns = [
    path('kub/',kub),
    path('XJIe6/', index),
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.sdghsdfh),
    path('archive/<int:years>/',archive),
    path('animales/',animales),
]
