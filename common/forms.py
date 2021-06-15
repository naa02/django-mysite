from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import Forest,Review

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        labels = {
            'content': 'Review 내용',
        }