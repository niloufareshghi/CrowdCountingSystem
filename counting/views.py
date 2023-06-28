from django.shortcuts import redirect, render
from counting.common import count_and_store
from counting.forms import ImageForm
from counting.models import Document, Submission
from threading import Thread
from pathlib import Path
from CowdCountingSystem.settings import STATIC_URL


def index(request):
    return redirect("home")


def upload(request):
    form = ImageForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data
            doc = Document(
                document=cd['document'],
                uploaded_at='',
                method=cd['method']
            )
            counting_sys = cd['method']
            submission = Submission(file=cd['document'], model=counting_sys)
            submission.save()
            Thread(
                target=count_and_store,
                kwargs={
                    "submission_id": submission.id,
                    "method": counting_sys,
                },
            ).start()

            return redirect("result", submission_id=submission.id)

    return render(request, "image_upload.html", {"form": form})


def result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)

    return render(
        request,
        "result.html",
        {
            "img_url": STATIC_URL + Path(submission.file.name).name,
            "submission": submission,
        },
    )


def home(request):

    return render(
        request,
        "home.html",
        {

        },
    )
