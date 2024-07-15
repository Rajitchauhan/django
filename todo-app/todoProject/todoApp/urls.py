from django.urls import path 
from . import views
urlpatterns = [
    path("" , views.home , name="home") , 
    path('register/' , views.register , name='register')  ,
    path('login/' , views.login_view , name='login') , 
    path('todos/' , views.todo_list , name='todos') , 
    path('addTodo/' , views.addTodo , name='addTodo') ,
     path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
     path('update_todo/<int:todo_id>/', views.update_todo, name='update_todo'),
]