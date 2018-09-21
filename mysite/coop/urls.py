from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dark', views.dark_index, name='dark')
]