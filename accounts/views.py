from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Student, Teacher

from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from django.views.decorators.csrf import csrf_exempt
from .serializer import UserSerializer, TeacherSerializer, StudentSerializer, _TeacherSerializer, _StudentSerializer 
from rest_framework import generics

from .permissions import IsTeacherOrReadOnly, IsPrinciple, IsPrincipleOrSelf


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
    serializer_class = _StudentSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPrinciple]
    
class TeacherListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = _TeacherSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPrinciple]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = _TeacherSerializer
    
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
    teacher = Teacher.objects.get(pk=pk)
    user = User.objects.get(pk=pk)
    return render(request, 'accounts/teacher_details.html',{'teacher': teacher, 'personal_data': user})

def studentprofile(request, pk):
    student = Student.objects.get(pk=pk)
    user = User.objects.get(pk=pk)
    return render(request, 'accounts/student_details.html', {'student': student, 'personal_data': user})


def getAllInSchool(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    
    return render(request, 'accoutns/all_in_school.html', {'students': student, 'teachers': teachers})