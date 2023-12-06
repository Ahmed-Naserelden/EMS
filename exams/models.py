from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import Student
# Create your models here.

class Exam(models.Model):
    subject = models.CharField(max_length=50)
    level = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),  # Change the limit_value as needed
            MaxValueValidator(4)  # Change the limit_value as needed
        ])
    
    questions = models.ManyToManyField('Question', related_name='exams')
    # decription = models.models.CharField(100, max_length=50, null=True, blank=True)
    
    def __str__(self):
	    return self.subject

class Question(models.Model):
    title = models.CharField(max_length=1000)
    answer = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),  # Change the limit_value as needed
            MaxValueValidator(4),  # Change the limit_value as needed
        ])
    
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    answer = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),  # Change the limit_value as needed
            MaxValueValidator(4),  # Change the limit_value as needed
        ]
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'exam', 'question'], name='unique_combination1')
        ]

class ExamAttempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    # Add other fields as needed
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'exam'], name='unique_combination2')
        ]


# Now I Want Serialize all models


