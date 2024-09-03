from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import category , task  
from .forms import taskform , categoryform , signupform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages




# Create your views here.

@login_required
def index(request) :
    categories = category.objects.all()
    tasks = task.objects.all()
    context = {
        "tasks" : tasks ,
        "categories" : categories
    }
    return render(request , "main/index.html" , context)


def detailed_task(request ,id):
    task1 = task.objects.get(id=id)
    context = {
        'task':task1
    }
    return render(request , 'main/detailed.html' , context)


def todo_by_status(request , st):
    todos = task.objects.filter(status = st)
    context = {
        'todos' :todos
    }
    return render(request , 'main/todosstatus.html' , context)


def get_task(request , cat) :
    task1 = task.objects.filter(category__name = cat)
    context = {
        'tasks' : task1
    }
    return render(request , "main/categories.html" , context)


def get_task_details(request , t_name) :
    details = task.objects.get(title = t_name)
    context = {
        'task' : details
    }
    return render(request , 'main/get_task_details.html' , context)


def createtodo(request) :
    if request.method == "POST" :
        form = taskform(request.POST)
        if form.is_valid() :
            task = form.save(commit=False)
            task.user = request.user
            form.save()
        return redirect("home")

    form = taskform()
    return render(request , "main/create_todo.html" , {"form" : form})


def create_category(request) :
    if request.method == "POST" :
        form = categoryform(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            form.save()
        return redirect("home")

    form = categoryform()
    return render(request , "main/create_category.html" , {"form" : form})


def update_todo(request , id) :
    task1 = get_object_or_404(task , id=id)
    if request.method == "POST" :
        form = taskform(request.POST , instance = task1)
        if form.is_valid() :
            form.save()
        return redirect("home")
    
    else :
        form = taskform(instance=task1)
        return render(request , "main/update_task.html" , {"form" : form})


def delete_todo(request , id) :
    task1 = get_object_or_404(task , id=id)
    task1.delete()
    return redirect("home")


def sign_up(request) :
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')  
    else:
        form = signupform()
    return render(request, 'registration/sign_up.html', {'form': form})


def logout_user(request) :
    logout(request)  
    messages.success(request, "You have been successfully logged out.") 
    return render(request, 'registration/logout.html', {
        'message': "You have been successfully logged out."
    })


def start(request) :
    error_message = ""
    if request.user.is_authenticated :
        return redirect("home")
    
    if request.method=="POST" :
        if "signup" in request.POST :
            return redirect("signup")
        
        elif "login" in request.POST :
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home") 
            else:
                error_message = "Incorrect username or password ! please enter your data again"
                
    return render(request , "main/start.html" , {"error_message" : error_message})
 
  