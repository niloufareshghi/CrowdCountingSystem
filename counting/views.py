import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from counting.forms import DocumentForm
from CrowdCountingModels import models


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            path = "documents/" + str(form.cleaned_data.get('document'))
            image_path = os.path.abspath(path)
            count = models.msfanet(image_path)
            return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, 'image_upload.html', {
        'form': form
    })
