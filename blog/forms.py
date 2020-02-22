from .models import Article
from django import forms

class CreateModelForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = (
            'reporter',
            'category',
            'title',
            'headline',
            'image',
            'content',
            )