from django.shortcuts import render , HttpResponse , redirect
from .forms import RegisterForm , TodoForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Todo
def home(request):
    return HttpResponse("HOME PAGE")

def login_view(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username , password=password)
            login(request , user)
            return redirect('todos')
    else:
        form = AuthenticationForm()
    return render(request , 'todoApp/login.html' , {'form' : form})

def register(request):
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username , password=password)
            login(request , user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request , 'todoApp/register.html' , {'form' : form})


def todo_list(request):
    todos = Todo.objects.filter(user = request.user)
    return render(request , 'todoApp/todo_list.html' , {'todos' : todos})



def addTodo(request):
    if request.method =='POST':
        form = TodoForm(request.POST)
        
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user 
            todo.save()
            return HttpResponse("DATA SAVED.....")
    else:
        form = TodoForm()
    return render(request , 'todoApp/todo_form.html' , {'form' : form})


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos')
    return render(request, 'todoApp/todo_confirm_delete.html', {'todo': todo})


def update_todo(request , todo_id):
    todo = Todo.objects.get(id=todo_id)
    
    if request.method == 'POST':
        form = TodoForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TodoForm(instance=todo)
    return render(request , 'todoApp/todo_form.html' , {'form' : form})




# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User

# Create User views here.
# def UserView(request):
#     users = User.objects.all()
#     password = 'password'
#     hashed_password = make_password(password)
#     return render(request, 'create_user.html', 
#                 {'users': users, 'hashed_password': hashed_password})
    
    
    