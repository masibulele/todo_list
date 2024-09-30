from django.shortcuts import render,redirect 
from django.contrib.auth.models import User 
from .models import Todo
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # get data from sign in form
        username = request.POST.get('name')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        #create user in database
        new_user = User.objects.create_user(username,email,pwd)
        new_user.save()

        return redirect(reverse('login'))
        
    return render(request,"signup.html")


def loginn(request):
    if request.method == "POST":
        #get data from form
        username = request.POST.get('name')
        pwd = request.POST.get('pwd')
        # print(username,pwd)
        user = authenticate(request,username=username,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('/index')
        else:
            return redirect('/login')
    
   
        
    return render(request,"login.html")

@login_required(login_url= '/loginn')
def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        obj = Todo(title=title, user=request.user)
        obj.save()
        res = Todo.objects.filter(user=request.user).order_by("-date")
        return redirect(reverse('index'),{'res':res})
    res = Todo.objects.filter(user=request.user).order_by("-date")
    return render(request,"index.html",{'res':res})


# edit to do list
@login_required(login_url= '/loginn')
def edit_todo(request,srno):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        obj = Todo.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect(reverse('index'))
    
    obj = Todo.objects.get(srno=srno)
    return render(request,"edit_todo.html",{'obj':obj})

@login_required(login_url= '/loginn')
def delete_todo(request,srno):
    obj = Todo.objects.get(srno=srno)
    obj.delete()
    return redirect(reverse('index'))


def signout(request):
    logout(request)
    return redirect(reverse('login'))