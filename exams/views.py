from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Exam, Question, StudentAnswer, ExamAttempt
from .serializer import ExamSerializer, QuestionSerializer, StudentAnswerSerializer, ExamAttemptSerializer, AnswersSerializer, StudentExamAnswerSerializer
from .permissions import IsTeacherOrReadOnly

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from EMS.views import signin as go_to_singin

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

# Create your views here.

class ExamList(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    authentication_classes = [BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsTeacherOrReadOnly]



class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacherOrReadOnly]
    
    # permission_classes = [IsAuthenticated]
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsTeacherOrReadOnly]
@api_view(['GET'])
def getAnswers(request, pk):
    questions = Exam.objects.get(pk=pk).questions.all()
    answers = AnswersSerializer(questions, many=True).data
    return Response(answers)

@api_view(['GET'])
def getStudAnswer(request, exam, student):
    answers = StudentAnswer.objects.filter(exam=exam, student=student)
    answers = StudentExamAnswerSerializer(answers, many=True).data
    return Response(answers)




class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacherOrReadOnly]
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsTeacherOrReadOnly]

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacherOrReadOnly]

    authentication_classes = [TokenAuthentication]   
    permission_classes = [IsTeacherOrReadOnly]


class StudentAnswerListCreateView(generics.ListCreateAPIView):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer


class StudentAnswerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer


class ExamAttemptListCreateView(generics.ListCreateAPIView):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer


class ExamAttemptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer
    
import EMS

def exam(request, pk):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    #  res = CostestQuestion.objects.filter(contest_id=pk)
    #     questions = [q.question_id for q in res]
    
    exam = Exam.objects.get(pk=pk)
    questions = exam.questions.all()
    print("questions => ", questions)
    return render(request, 'exams/exam.html', {'questions': questions, "contest_id": pk, "subject": exam.subject})
    # return redirect(go_to_singin)
def exams(request):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    is_teacher = request.user.groups.filter(name='Teacher_Group').exists()
    is_manager = request.user.groups.filter(name='Principle').exists()
    
    contests = Exam.objects.all()
    return render(request, 'exams/exams.html', {'contests': contests, "manger": is_manager, "is_teacher": is_teacher})
    
    messages.info(request, 'you must Login')
    return redirect(go_to_singin)

def addexam(request):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    return render(request, 'exams/add_exam.html', {})


def editexam(request, pk):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    exam = Exam.objects.get(pk=pk)
    exam = ExamSerializer(exam).data
    

    return render(request, 'exams/edit_exam.html', {"exam": exam, 'pk': pk})

require_POST
def deletexam(request, pk):
    if request.user.is_anonymous == True:
        return redirect(EMS.views.signin)
    
    exam = get_object_or_404(Exam, pk=pk)
    exam.delete()
    return redirect(exams)