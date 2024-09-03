from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import loginform


urlpatterns = [
    path('' , start , name='start'),
    path('/index/' , index , name='home'),
    path('detailed/<int:id>' , detailed_task , name = 'detail'),
    path('todos/status/<str:st>' , todo_by_status , name = 'status'),
    path('category/<str:cat>/tasks' , get_task , name="category"),
    path('task/<str:t_name>/details' ,get_task_details , name='t_details' ),
    path('todo/create' , createtodo , name="createtodo"),
    path('category/create' , create_category , name="createcategory"),
    path('todo/update<int:id>' , update_todo , name="updatetodo"),
    path('todo/delete<int:id>' , delete_todo , name="deletetodo"),
    path('signup/', sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=loginform), name='login'),
    path('logout/', logout_user, name='logout'),
]