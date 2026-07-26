from django.urls import path
from.import views
app_name='bookverse'
from django.urls import path
from . import views

app_name = 'bookverse'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_list, name='book_list'),
]

