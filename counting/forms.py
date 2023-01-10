from django import forms
from counting.models import Document
import os
from django.core.exceptions import ValidationError

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )

    def clean(self):
        file_path = "documents/" + str(self.cleaned_data.get('document'))
        path = os.path.abspath(file_path)
        return self.cleaned_data

