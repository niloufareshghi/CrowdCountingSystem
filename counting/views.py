import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from counting.forms import DocumentForm
from CrowdCountingModels import models
from counting.models import FileModel


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
            print(count)
            return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, 'image_upload.html', {
        'form': form
    })


def api(request):
    file_model = FileModel()
    _, file = request.FILES.popitem()  # get first element of the uploaded files

    file = file[0]  # get the file from MultiValueDict

    file_model.file = file
    file_model.save()

    return HttpResponse(content_type='text/plain', content='File uploaded')
