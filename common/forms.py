from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import Forest,Comment2

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

class Comment2Form(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ['content']
        labels = {
            'content': 'Comment 내용',
        }