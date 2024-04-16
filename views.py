from django.shortcuts import render
from django.http import HttpResponse
from .form import moviereviewform,commentform,RegisterForm
from .models import movie,comments
# from django.shortcuts import render
# from .form import RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def moviereview(request):
    form=moviereviewform()
    if request.method=='POST' and request._files:
        form=moviereviewform(request.POST,request._files)
        if form.is_valid():
            form.save()
        return HttpResponse('Movie Review Inserted Successfully')
    return render(request,'movieinsert.html',{'form':form})


def displayall(request):
    data=movie.objects.all()
    return render(request,'home.html',{'data':data})

@login_required(login_url='/login/')
def displayone(request,id):
    data=movie.objects.get(id=id)
    form=commentform(initial={'review':id})
    comment=comments.objects.filter(review_id=id)
    if request.method=='POST':
        form1=commentform(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'single.html',{'data':data,'form':form,'comment':comment})


def homepageview(request):
    return render(request,'homepage.html')


def RegisterView(request):
    form=RegisterForm
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            password=form.password
            form.password=make_password(password)
            form.save()
            return HttpResponse('Register successflly')
    return render(request,'register.html',{'form':form})

def LoginView(request):
    form=AuthenticationForm
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            data=movie.objects.all()
            return render(request,'home.html',{'data':data})
        else:
            form=RegisterForm
            if request.method=='POST':
                form=RegisterForm(request.POST)
                if form.is_valid():
                    form=form.save(commit=False)
                    password=form.password
                    form.password=make_password(password)
                    form.save()
                    return HttpResponse('Register successfully')
            return render(request,'register.html',{'form':form})
    return render(request,'login.html',{'form':form})

@login_required(login_url='/login/')
def logoutview(request):
    logout(request)
    return render(request,'logout.html')



def videoview(request):
    return render(request,'video.html')