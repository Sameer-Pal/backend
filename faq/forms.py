from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
        widgets = {
            'answer': CKEditorWidget(),  # Use CKEditor for rich text answer input
        }
