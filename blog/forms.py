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

class BlogForm(forms.Form):
    reporter=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Author name'
    }
    ))
    category=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Category'
    }
    ))
    title=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Post title'
    }
    ))
    headline=forms.CharField(max_length=200,widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Headline',
        'cols':30,
        'rows':6}
        ))
    image=forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control',
        'placeholder':'image'
    }
    ))
    content=forms.CharField(max_length=200,widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'content or body',
        'cols':30,
        'rows':6
    }
    ))
