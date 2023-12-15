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


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="report")
    issue = models.CharField(max_length=255)
    level = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),  # Change the limit_value as needed
            MaxValueValidator(4)  # Change the limit_value as needed
        ]
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.issue}"
    

        
