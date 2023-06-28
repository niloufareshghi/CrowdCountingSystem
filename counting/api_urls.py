from django.urls import path

from . import api_views

urlpatterns = [
    # path('', views.index, name='index'),
    path("upload_api", api_views.upload, name="upload"),
    path("result_api/<int:submission_id>", api_views.result, name="result"),
]
