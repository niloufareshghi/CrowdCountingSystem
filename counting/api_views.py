import os
from threading import Thread
from django.views.decorators.http import require_http_methods
from counting.common import count_and_store
from django.http import JsonResponse

from counting.forms import DocumentForm
from counting.models import Submission


@require_http_methods(["POST"])
def upload(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        path = "uploaded_files/" + str(form.cleaned_data.get("document"))
        image_path = os.path.abspath(path)

        submission = Submission(file=image_path)
        submission.save()
        Thread(
            target=count_and_store,
            kwargs={
                "submission_id": submission.id,
            },
        ).start()

        return JsonResponse({"submission_id": submission.id})

    return JsonResponse({"submission_id": -1})


@require_http_methods(["GET"])
def result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)

    return JsonResponse(
        {
            "status": submission.status,
            "count": submission.count,
            "message": submission.message,
        }
    )
