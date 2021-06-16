from django import forms
from django.forms import fields
from nature.models import Forest,Comment2

class Comment2Form(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ['content']
        labels = {
            'content': 'Comment 내용',
        }