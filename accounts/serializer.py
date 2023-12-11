from rest_framework import serializers
from .models import Student, Teacher
from django.contrib.auth.models import User, Group

# from accounts.employerSerializers import TeacherSerializer, StudentSerializer 

class _UserSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(required=False)
    # teacher = TeacherSerializer(required=False)
    user_type = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'student', 'teacher', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')

        if user_type == 'student':
            student_data = validated_data.pop('student', {})
            user = User.objects.create_user(**validated_data)
            student = Student.objects.create(user=user, phone=student_data['phone'], level=student_data['level'])
            return student

        else:
            teacher_data = validated_data.pop('teacher', {})
            # print(teacher_data)
            # print(validated_data)

            user = User.objects.create_user(**validated_data)
            
            teacher = Teacher.objects.create(user=user, phone=teacher_data['phone'], role=teacher_data['role'])
            teachers_group, created = Group.objects.get_or_create(name='Teacher_Group')
            user.groups.add(teachers_group)
            return teacher

        return None
    



class _StudentSerializer(serializers.ModelSerializer):
    user = _UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}



class StudentSerializer(serializers.ModelSerializer):
    # user = _UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}



class _TeacherSerializer(serializers.ModelSerializer):
    user = _UserSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'
        
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}



class UserSerializer(serializers.ModelSerializer):
    student = StudentSerializer(required=False)
    teacher = TeacherSerializer(required=False)
    user_type = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'student', 'teacher', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')

        if user_type == 'student':
            student_data = validated_data.pop('student', {})
            user = User.objects.create_user(**validated_data)
            student = Student.objects.create(user=user, phone=student_data['phone'], level=student_data['level'])
            return student

        else:
            teacher_data = validated_data.pop('teacher', {})
            # print(teacher_data)
            # print(validated_data)

            user = User.objects.create_user(**validated_data)
            
            teacher = Teacher.objects.create(user=user, phone=teacher_data['phone'], role=teacher_data['role'], salary=teacher_data['salary'])
            teachers_group, created = Group.objects.get_or_create(name='Teacher_Group')
            user.groups.add(teachers_group)
            return teacher

        return None
    
