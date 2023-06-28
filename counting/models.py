from django.db import models
from django.db.models import FileField, DateTimeField


class Document(models.Model):
    document = models.FileField()
    uploaded_at = models.DateTimeField()
    method = models.CharField(max_length=10, default="")


class Submission(models.Model):
    file = FileField(upload_to="uploaded_files/", default="")
    model = models.CharField(max_length=10, default="")
    SUBMITTED = 0
    RUNNING = 1
    SUCCESS = 2
    FAILED = 3
    STATUS_CHOICES = [(0, "Submitted"), (1, "Running"), (2, "Success"), (3, "Failed")]
    status = models.IntegerField(choices=STATUS_CHOICES, default=SUBMITTED)
    count = models.IntegerField(default=0)
    predict = models.CharField(default="", max_length=50)
    message = models.CharField(default="", max_length=100)
    model_name_desc = models.CharField(default="", max_length=250)
