from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

# from exams import views as ev
import exams
from accounts.models import Principle, Student


# # Create your views here.


def signin(request):

    if request.user.is_anonymous == False:
        return redirect(exams.views.exams)
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(request.user.get_all_permissions())
        if user is not None:
            login(request, user)
            return redirect(exams.views.exams)
            # pass
        else:
            messages.info(request, 'User is not Exist')
    return render(request, 'login.html')

def signup(request):
    if request.user.is_anonymous == False:
        return redirect(exams.views.exams)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = form.data['username']
        phone = request.POST['phone']
        level = request.POST['level']
        email = request.POST['email']
        print('form.username', username)
        print('Level: ', level)

        if form.is_valid():
            try:
                form.save()
                user = User.objects.get(username=username)
                try:
                    student = Student(user=user, phone=phone, level=level)
                    student.save()
                    print("<<<<<<<<<<< Saved >>>>>>>>>>>")
                    user.email = email
                    user.save()
                except:
                    user.delete()
                    messages.info(request,'Register is not Successfully')
                    return redirect(signup)
                return redirect(signin)
            except:
                messages.info(request,'Register is not Successfully')
        else:
            messages.info(request,'Register is not Successfully')

    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    if request.user.is_anonymous == True:
        return redirect(signin)
    return render(request, 'home.html')

def signout(request):
    logout(request)
    return redirect(signin)