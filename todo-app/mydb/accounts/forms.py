from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from .models import Todo , Feedback

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["advice", "good", "user"]