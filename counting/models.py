from django.db import models
from django.db.models import FileField, DateTimeField


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class FileModel(models.Model):
    file = FileField(upload_to='uploaded_files/', default='')
    created = DateTimeField(auto_now=True)
