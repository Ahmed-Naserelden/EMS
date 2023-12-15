from rest_framework import serializers
from django.contrib.auth.models import User
from .designpatterns import Monitor, Level1Exam, Level2Exam, Level3Exam #, MonthExam, FinalExam
from .models import Exam, Question, ExamAttempt, StudentAnswer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['pk', 'answer']

class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    # questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'
        
    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        # examkind = validated_data.pop('examkind')
        
        # exam = Exam.objects.create(**validated_data)
        # for question_data in  questions_data:
        #     q = Question.objects.create(**question_data)
        #     exam.questions.add(q)
        
        
        exam = Level1Exam()
        if validated_data['level'] == 2:
            exam = Level2Exam()
        elif validated_data['level'] == 3:
            exam = Level3Exam()
        monitor = Monitor(exam)
        
        return monitor.createExam(validated_data, questions_data)
    
    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.level = validated_data.get('level', instance.level)
        instance.save()
        questions_data = validated_data.pop('questions')
        instance.questions.all().delete()
        for question_data in  questions_data:
            q = Question.objects.create(**question_data)
            instance.questions.add(q)
        
        return instance

class StudentAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentAnswer
        fields = '__all__'

class ExamAttemptSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamAttempt
        fields = '__all__'


class StudentExamAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ['pk', 'question', 'answer']