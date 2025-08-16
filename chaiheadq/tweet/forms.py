from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        # We are creating this fields in Array because we are using custom forms
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # We are creating this fields in tuple because we are using built in django forms
        fields = ('username','email','password1','password2')

class SearchForm(forms.Form):
    query = forms.CharField(
    label = 'Search Your Tweet',
    required = False,
    max_length = 100,

    )