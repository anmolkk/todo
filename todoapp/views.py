from django.shortcuts import render,redirect
from .forms import todo_Forms,user_form
from .models import ToDo
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="login")
def index(request):
    tasks = ToDo.objects.all() 
    form =   todo_Forms()
    if request.method == "GET":
        return render(request,"todo.html",{'form':form, "tasks":tasks})
    else:
        data = todo_Forms(request.POST)

        print(data["time"].value())
        try:
            forms = ToDo(user =request.user,task=data["task"].value(), time = data["time"].value())
            forms.save()
        except Exception:
            pass
            # forms = ToDo(user =request.user, task = task, time=None)
            # forms.save()
        
    return render(request,"todo.html", {"form":form, "tasks":tasks})

@login_required(login_url="login")
def dlttask(request, id):
    dlt = ToDo.objects.get(id = id)
    dlt.delete()
    return redirect("todo")

@login_required(login_url="login")
def edittask(request,id):
    data = ToDo.objects.get(id=id)
    tasks = ToDo.objects.all()  
    if request.method == "GET":
        form = todo_Forms(instance=data)
        return render(request, "todo.html", {"form":form, "tasks":tasks})
    else:
        taskn = todo_Forms(request.POST,instance=data)
        if taskn.is_valid:
            taskn.save()
        return redirect("todo")

def login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("todo")
        else:
            messages.info(request, "Please Enter the correct Credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def register(request):
    form = user_form()
    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists")
                return render(request,"register.html",{"form":form})
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return render(request,"register.html",{"form":form})
            data = User.objects.create_user(username=username , email=email, password=password)
            data.save()
            return redirect("login")
    else:
        return render(request,"register.html",{"form":form, })
    
def logout(request):
    auth.logout(request)
    return redirect("home")