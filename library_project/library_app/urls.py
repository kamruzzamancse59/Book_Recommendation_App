from django.urls import path
from . import views
from library_app import views 

urlpatterns = [
    path('', views.search_books, name='search_books'),
   
]