# admin.py

from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FaqAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditorWidget(),
        }
class FaqAdmin(admin.ModelAdmin):
    form = FaqAdminForm

admin.site.register(FAQ, FaqAdmin)
