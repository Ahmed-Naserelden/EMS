from django.urls import path, include
from .views import ExamList, ExamDetail, QuestionList, QuestionDetail
from . import views
urlpatterns = [
    path('exams/', ExamList.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetail.as_view(), name='exam-detail'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    
    path('student-answers/', views.StudentAnswerListCreateView.as_view()),
    path('student-answers/<int:pk>/', views.StudentAnswerRetrieveUpdateDestroyView.as_view()),

    path('exam-attempts/', views.ExamAttemptListCreateView.as_view()),
    path('exam-attempts/<int:pk>/', views.ExamAttemptRetrieveUpdateDestroyView.as_view()),
    
    path('exam/<int:pk>', views.exam, name='exam'),
    path('addexam/', views.addexam, name='addexam'),
    path('editexam/<int:pk>/', views.editexam, name='editexam'),

    path('', views.exams, name='exams'),
    
    path('deletexam/<int:pk>', views.deletexam, name='deletexam'),
    path('exam/answers/<int:pk>', views.getAnswers, name='answers'),
    path('exam/answers/<int:exam>/<int:student>', views.getStudAnswer, name='student-answers'),
]
