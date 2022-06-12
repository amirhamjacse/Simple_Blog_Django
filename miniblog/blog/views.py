from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, Add_Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.
#Home page
def HomePage(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts })
#About Page
def AboutPage(request):
    return render(request, 'blog/about.html')
#Dashboard Page
def DashboardPage(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts': posts,
        'fn': full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
#Login Page
def LoginPage(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Sussesfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')
#Signup Page
def SignupPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation You are Author Now')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)

    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})
#Contact Page
def ContactPage(request):
    return render(request, 'blog/contact.html')
#Logout Page
def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')
#Add New Post
def AddPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Add_Post(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                messages.success(request, 'Post Added Successfully')
                form = Add_Post()
        else:
            form = Add_Post()
        return render(request, 'blog/addpost.html', {'forms':form})
    else:
        return HttpResponseRedirect('/login/')

#Updatepost
def UpdatePost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = Add_Post(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Updated Successfully')
        else:
            pi = Post.objects.get(pk=id)
            form = Add_Post(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
#del post
def Delpost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')