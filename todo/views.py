from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Tasks
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        
        print(fnm,emailid,pwd)

        my_user = User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm,pwd)
        my_user = authenticate(request,username=fnm, password=pwd)
        if my_user is not None:
            login(request, my_user)
            return redirect('/home')
        else:
            return redirect('/login')
        
    return render(request, 'login.html')

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print(title,desc)
        my_task = Tasks(title=title, desc=desc, user=request.user)
        my_task.save()
        tasks = Tasks.objects.filter(user=request.user)
        return redirect('/home', {'tasks':tasks})
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'home.html',{'tasks':tasks})

@login_required(login_url='/login')
def todo_update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print(title,desc)
        my_task = Tasks.objects.get(srno=id)
        my_task.title = title
        my_task.desc = desc
        my_task.save()
        # tasks = Tasks.objects.filter(user=request.user)
        return redirect('/home' )
    my_task = Tasks.objects.get(srno=id)
    # tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'todo_update.html',{'my_task':my_task})

@login_required(login_url='/login')
def todo_delete(request, id):
    my_task = Tasks.objects.get(srno=id)
    my_task.delete()
    return redirect('/home')

def signout(request):
    logout(request)
    return redirect('/login')