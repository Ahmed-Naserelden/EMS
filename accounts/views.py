from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Student, Teacher, Notification
from django.contrib import messages

from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from django.views.decorators.csrf import csrf_exempt
from .serializer import UserSerializer, TeacherSerializer, StudentSerializer, _TeacherSerializer, _StudentSerializer 
from rest_framework import generics

from .permissions import IsTeacherOrReadOnly, IsPrinciple, IsPrincipleOrSelf

import EMS

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# ///////////////////API////////////////////////

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = _StudentSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacherOrReadOnly]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPrinciple]
    
class TeacherListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPrinciple]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPrinciple]

# ///////////////////////////////////////////

# Create your views here.
def create_user(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return user

@api_view(['POST'])
def signup(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user_type = serializer.validated_data.get('user_type')

        if user_type == 'student':
            student = serializer.save()
            # token, created = Token.objects.get_or_create(user=student)
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)

        else:
            teacher = serializer.save()
            return Response(TeacherSerializer(teacher).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow any user (authenticated or not) to access this view
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'Authentication successful', 'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signout(request):
    # Logout the user
    logout(request)

    return Response({'message': 'Logout successful'}, status=200)

def teacherprofile(request, pk):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    if request.method == 'POST':
        salary = request.POST['salary']
        phone = request.POST['phone']
        role = request.POST['major']
        username = request.POST['username']
        
        teacher = Teacher.objects.get(user = User.objects.get(username=username))
        teacher.salary = salary
        teacher.phone = phone
        teacher.role = role
        
        teacher.save()

    
    is_teacher = request.user.groups.filter(name='Teacher_Group').exists()
    is_manager = request.user.groups.filter(name='Principle').exists()
    
    teacher = Teacher.objects.filter(pk=pk)
    user = User.objects.get(pk=pk)
    
    if not teacher:
        return HttpResponse("Not Exist");
    
    teacher = teacher[0]
    
    return render(request, 'accounts/teacher_details.html',{'teacher': teacher, 'personal_data': user, "manger": is_manager, "is_teacher": is_teacher})

def studentprofile(request, pk):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    is_teacher = request.user.groups.filter(name='Teacher_Group').exists()
    is_manager = request.user.groups.filter(name='Principle').exists()
    
    student = Student.objects.filter(pk=pk)
    user = User.objects.get(pk=pk)
    
    if not student:
        return HttpResponse("Not Exist");
    student = student[0]
    
    return render(request, 'accounts/student_details.html', {'student': student, 'personal_data': user, "manger": is_manager, "is_teacher": is_teacher})

def getAllInSchool(request):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    is_teacher = request.user.groups.filter(name='Teacher_Group').exists()
    is_manager = request.user.groups.filter(name='Principle').exists()
    
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    
    return render(request, 'accounts/all_in_school.html', {'students': students, 'teachers': teachers, "manger": is_manager, "is_teacher": is_teacher})

def addteacher(request):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        role = request.POST['major']
        email = request.POST['email']
        salary = request.POST['salary']
        try:
            user = User(username=username, password=password, email=email)
            user.save()
            try:
                teacher = Teacher(user=user, phone=phone, role=role, salary=salary)
                teacher.save()
            except:
                user.delete()
                messages.info(request,'Register is not Successfully2')
        except:
            messages.info(request,'Register is not Successfully1')
            
    return render(request, 'accounts/add_teacher.html', {})

def myprofile(request):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    is_teacher = request.user.groups.filter(name='Teacher_Group').exists()
    is_manager = request.user.groups.filter(name='Principle').exists()
    
    if request.user.groups.filter(name='Teacher_Group').exists() or request.user.pk == 1:
        user = request.user;
        teacher = Teacher.objects.get(pk=request.user.pk)
        return render(request, 'accounts/teacher_details.html', {'teacher': teacher, 'personal_data': user, "hide": True, "manger": is_manager, "is_teacher": is_teacher})
    else:
        user = request.user;
        student = Student.objects.get(pk=request.user.pk)
        return render(request, 'accounts/student_details.html', {'student': student, 'personal_data': user, 'hide': True, "manger": is_manager, "is_teacher": is_teacher})
    


from .designpatterns import Factor, WhatsAppNotification
    
def notifications(request):
    if request.method == 'POST':
        message = request.POST['message']
        level = request.POST['level']
        
        factor = Factor()
        way = factor.sendNotification('web')
        way.setMessage(message)
        way.setLevel(level)
        way.send()
        
        
        # students = Student.objects.filter(level=level)
        # for stude  in students:
        #     noti = Notification(student=stude, message=message)
        #     noti.save()
        
        
        return render(request, 'notifications.html')
    
    else :
        try:
            stude = Student.objects.get(user=request.user)
            notifications = Notification.objects.filter(student=stude) #, is_read=False).order_by('-created_at')
            
            context = {
                "notifications": notifications,
                "is_student": True
            }

            return render(request, "notifications.html", context)
        except:
            pass
       
    return render(request, "notifications.html", {"is_teacher": True})

def mark_as_read(request, notification_id):
    try:
        stude = Student.objects.get(user=request.user)
        notification = Notification.objects.get(pk=notification_id, student=stude)
        notification.is_read = True
        notification.save()
    except Notification.DoesNotExist:
        pass
    return redirect("notifications")