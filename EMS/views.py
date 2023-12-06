from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# from exams import views as ev
import exams
from accounts.models import Principle
# # Create your views here.

def signin(request):

    if request.user.is_anonymous == False:
        # if request.user != 'admin':
        pass
        # return redirect(cv.contests)
        # else: 
        #     return redirect(manage)
        
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
    # if request.user.is_anonymous == False:
    #     return redirect(cv.contests)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # form = SignUpForm(request.POST)
        username = form.data['username']
        u_name = request.POST['user_name']
        phone = request.POST['phone']
        level = request.POST['level']

        print('form.username', username)
        print('Name: ', u_name)
        print('Level: ', level)

        if form.is_valid():
            form.save()
            user = User.objects.get(username=username)
            # student = Student(id=user, level=level, name=u_name,)
            # student.save()
            # """
            return redirect(signin)
        else:
            messages.info(request,'Register is not Successfully')

    form = UserCreationForm()
    
    # form = SignUpForm()
    return render(request, 'register.html', {'form': form})