from django.urls import path

from XJIe6.views import index,archive, kub, animales, negroid
from . import views

urlpatterns = [
    path('kub/',kub),
    path('', index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.sdghsdfh),
    path('archive/<int:years>/',archive),
    path('animales/',animales),
    path('book/<slug:book_slug>/', views.show_book,name = 'book'),
    path('negroid/',negroid),
]