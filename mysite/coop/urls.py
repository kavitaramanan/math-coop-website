from django.urls import path
from django.conf.urls.static import static

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outreach', views.outreach, name='outreach'),
    path('people', views.people, name="people"),
    path('manage/', views.manage, name="manage"),
    path('manage/pres', views.manage_pres, name='manage_pres'),
    path('manage/outreach', views.manage_outreach, name='manage_outreach'),
    path('manage/people', views.manage_people, name='manage_people'),
    path('manage/topics', views.manage_topics, name='manage_topics'),
    path('manage/upload/pres', views.upload_pres, name='upload_pres'),
    path('manage/upload/outreach', views.upload_outreach, name='upload_outreach'),
    path('manage/upload/person', views.add_person, name='add_person'),
    path('manage/upload/topic', views.upload_topic, name='upload_topic'),
    path('manage/edit/pres/', views.edit_pres, name='edit_pres'),
    # path('manage/edit/outreach', views.edit_outreach, name='edit_outreach'),
    # path('manage/edit/person', views.edit_person, name='edit_person'),
    # path('manage/edit/topic', views.edit_topic, name='edit_topic'),
    path('delete', views.delete, name='delete'),
    path(r'download/ppts/(file_name>.+)', views.download, name="download"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)