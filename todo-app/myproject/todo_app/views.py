from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'todo_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'todo_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'todo_app/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'todo_app/profile.html', {'name': request.user.username})

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) # why commit is False
            todo.user = request.user
            todo.save()
            return redirect('list_todos')
    else:
        form = TodoForm()
    return render(request, 'todo_app/todo_form.html', {'form': form})

@login_required
def list_todos(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

@login_required
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list_todos')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_app/todo_form.html', {'form': form})

@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('list_todos')
    return render(request, 'todo_app/todo_confirm_delete.html', {'todo': todo})
