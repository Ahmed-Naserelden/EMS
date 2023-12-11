from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=11, unique=True)
    level = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),  # Change the limit_value as needed
            MaxValueValidator(4)  # Change the limit_value as needed
        ]
    )

    def __str__(self):
        return self.user.username
    

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=11)
    role = models.CharField(max_length=11)
    salary = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    
    def __str__(self):
        return self.user.username


# sothat when usercreated create token automatic.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        


class Notification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.message}"

    class Meta:
        ordering = ["-created_at"]



from abc import ABCMeta, abstractmethod

class Employee():

    def __init__(self, name, email, phone, password):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__password = password

    def getName(self):
        return self.__name
    
    def getPhone(self):
        return self.__phone
    
    def getPassword(self):
        return self.__password
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email
    
    def setPhone(self, phone):
        self.__phone = phone

    def setName(self, name):
        self.__name = name

    def setPassword(self, password):
        self.__password = password



class Teachero(Employee):
    
    def __init__(self, name, email, phone, password, salary, role):
        super().__init__(name, email, phone, password)
        self.__salary = salary
        self.__role = role

    def setSalay(self, salary:float):
        self.__salary = salary

    def getSalary(self) -> float:
        return self.__salary
    
    def setRole(self, role:str):
        self.__role = role

    def getRole(self) -> str:
        return self.__role



# SingleTon
class Principle(Teachero, object):

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        
        if not cls._instance:
            cls._instance = super(Principle, cls).__new__(cls)
            
        return cls._instance

    def __init__(self, name, email, phone, password, salary, role):
        
        if not hasattr(self, 'initialized'):
            
            super(Principle, self).__init__(name, email, phone, password, salary, role)
            self.initialized = True

    def creatU(self, name, password):
        u = User(username=name, password=password)
        u.save()
        print("Hello")

# class Student(Employee):
    
#     def __init__(self, name, email, phone, password, level):
#         super().__init__(name, email, phone, password)
#         self.__level = level

#     def getLevel(self):
#         return self.__level
    
#     def setLevel(self, level):
#         self.__level = level

        
