from django.shortcuts import render , redirect , HttpResponse
from .forms import RegisterForm ,  LoginForm , TodoForm ,   FeedbackForm
from django.contrib.auth import login , authenticate
from .models import Todo , Feedback

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def LogiView(request):
    if request.method == "POST":
        form = LoginForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})



def showTodos(request):
    todos = Todo.objects.all()
    return render(request, 'todo.html' , {"todos": todos})

def profile(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'profile.html' , {"user": request.user, "todos": todos})


def AddTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) # why commit is False
            todo.user = request.user
            todo.save()
            return redirect('todos')
    else:
        form = TodoForm()
    return render(request, 'todoForm.html', {'form': form})


def deleteTodo(request , idTodo):
    todo = Todo.objects.get(id = idTodo)
    if request.method == 'POST':
        todo.delete()
        return redirect('profile')
        
    return render(request, 'todo_confirm_delete.html', {'todo': todo})

def update(request , idTodo):
    todo = Todo.objects.get(id = idTodo)
    if request.method == 'POST':
        form = TodoForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoForm.html' , {'form': form})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})
