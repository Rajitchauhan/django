from django.urls import path
from . import views
urlpatterns = [
    path('home', views.homepage, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.LogiView, name='login') ,
    path('todos/', views.showTodos, name='todos') ,
    path('profile/', views.profile, name='profile') ,
    path('AddTodo/', views.AddTodo, name='AddTodo') , 
    path('deleteTodo/<int:idTodo>/', views.deleteTodo, name='deleteTodo') ,
    path('update/<int:idTodo>/', views.update, name='update') ,
    path('feedback/', views.feedback , name='feedback') ,
       
# <int:todo_id>/

]
