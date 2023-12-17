from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^download/(?P<file_path>.*)/$', views.file_response_download, name="downloadFile"),
]