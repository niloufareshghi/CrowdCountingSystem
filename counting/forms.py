from django import forms
import os
from django.core.exceptions import ValidationError

from django import forms

CHOICES = [
    ('msfa', 'MSFANet'),
    ('can', 'CAN'),
    ('p2p', 'P2PNet'),
    ('smart', 'Smart'),
    ]


class ImageForm(forms.Form):
    document = forms.FileField()
    method = forms.CharField(label='Choose Your Desired Crowd Counting Method', widget=forms.Select(choices=CHOICES))

    def clean(self):
        file_path = "uploaded_files/" + str(self.cleaned_data.get("document"))
        path = os.path.abspath(file_path)
        return self.cleaned_data
