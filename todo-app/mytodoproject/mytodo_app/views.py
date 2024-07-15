from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import login , authenticate
from .forms import RegisterForm , LoginForm

# Create your views here.

def home(request):
    return render(request , 'home.html')
    # return HttpResponse("this is home page")
    
    
def register(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            
            user = authenticate(username = username , password=password)
            login(request , user)
            return redirect('profile')
    else:
        forms = RegisterForm()
    return render(request , 'register' , {'forms' : forms})

def login_view(request):
    if request.method == 'POST':
        forms = LoginForm(request , data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            
            user = authenticate(username=username , password=password)
            
            if user is not None:
                login(request , user)
                return redirect('profile')
    else:
        forms = LoginForm()
        
    return render(request , 'login.html' , {'forms' : forms})


def profile(request):
    return render(request , 'profile.html')

def todo_list(request):
    return render(request , 'todo_list.html')