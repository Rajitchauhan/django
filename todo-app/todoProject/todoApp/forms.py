from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from .models import Todo
from django import forms

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['username' , 'password1' , 'password2']
        

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        



