from  django.urls import path 
from . import views
urlpatterns = [
    path('' , views.home , name="home"),
    path('login_view/' , views.login_view , name="login_view") ,
    path('register/' , views.register , name='register') , 
    path('profile' , views.profile , name='profile') , 
    path('todo_list' , views.todo_list , name='todo_list') , 
    
]