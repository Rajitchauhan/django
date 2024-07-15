from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('todos/', views.list_todos, name='list_todos'),
    path('todo/add/', views.add_todo, name='add_todo'),
    path('todo/update/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
