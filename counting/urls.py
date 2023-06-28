from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("home", views.home, name='home'),
    path("upload", views.upload, name="upload"),
    path("result/<int:submission_id>", views.result, name="result"),
]
