from django.contrib import admin
from .models import Question, Exam, ExamAttempt, StudentAnswer

# Register your models here.

admin.site.register(Question)
admin.site.register(Exam)

admin.site.register(ExamAttempt)
admin.site.register(StudentAnswer)