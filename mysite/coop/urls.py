from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outreach', views.outreach, name='outreach'),
    path('manage', views.management, name='manage'),
    path('upload_pres', views.upload_pres, name='upload_pres'),
    path('upload_outreach', views.upload_outreach, name='upload_outreach')
]