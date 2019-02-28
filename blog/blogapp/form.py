from django import forms
from .models import Blog

class BlogPost(forms.Form):
    image = forms.ImageField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    Rates = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')])