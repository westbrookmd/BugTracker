from django import forms
from . import models

class CreateBug(forms.ModelForm):
    class Meta:
        model = models.Bugs
        fields = ['title', 'body', 'slug', 'class_name', 'thumb']
        
