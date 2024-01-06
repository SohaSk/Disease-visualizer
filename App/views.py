from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import signupForm
from .models import Diseases,User
from django.contrib import messages

#from .admin import UserAdmin

# Create your views here.
def home(request):
    return render(request,'home.html')

@csrf_exempt
def signup(request):
    fm = signupForm()
    if request.method == 'POST':
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    return render(request,'Signup.html',{'form':fm})



@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=User.objects.values_list('username',flat=True)
        if username in list(user):
            user_password = User.objects.filter(username=username).values_list('password', flat=True)[0]
            if password==user_password:
                return redirect('home')
            else:
                messages.info(request, 'Username or password incorrect')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request,'login.html')


@csrf_exempt
def search(request):
    if request.method=="POST":
        if 'searched' in request.POST:
            searched=request.POST['searched']
            post = Diseases.objects.filter(Disease_Name__contains=searched)
            return render(request,'search.html',{'searched':searched,'post':post})
    else:
        return render(request, 'search.html', {})



def search1(request):
    post = Diseases.objects.filter(Disease_Name__contains='covid')
    return render(request, 'search1.html', {'post': post})

def search2(request):
    post = Diseases.objects.filter(Disease_Name__contains='hiv')
    return render(request, 'search2.html', {'post': post})

def search3(request):
    post = Diseases.objects.filter(Disease_Name__contains='diabetes')
    return render(request, 'search3.html', {'post': post})

def search4(request):
    post = Diseases.objects.filter(Disease_Name__contains='breast cancer')
    return render(request, 'search4.html', {'post': post})

def dash2(request):
    return render(request,'dash2.html')


def dash4(request):
    return render(request,'dash4.html')

def dash5(request):
    return render(request,'dash5.html')

def dash6(request):
    return render(request,'dash6.html')