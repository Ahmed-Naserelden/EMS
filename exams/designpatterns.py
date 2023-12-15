from abc import ABCMeta, abstractmethod
from .models import Exam as Quiz, Question
# Builder Design Patterns
class Exam:
    
    def __init__(self, kind, duration):
        self.__kind = kind
        self.__duration = duration
    
    def setDuration(self, duration):
        self.__duration = duration
    
    def getDuration(self):
        return self.__duration
    
    def setKind(self, kind):
        self.__kind = kind
    def getKind(self):
        return self.__kind

    def setExamDetails(self, examdetails):
        self.__examdetails = examdetails    
    def setQuestions(self, questions_data):
        self.__questions_data = questions_data

    def save(self):
        exam = Quiz.objects.create(**self.__examdetails)

        for question in self.__questions_data:
            q = Question.objects.create(**question)
            exam.questions.add(q)

        return exam

    def __str__(self):
        return f"{self.__examdetails['subject']}\n{self.__examdetails['level']}"

class ExamBuilder(metaclass=ABCMeta):
    def __init__(self, kind, duration):
        self.__exam = Exam(kind, duration)
    
    def getExam(self):
        return self.__exam
    
    @abstractmethod
    def buildQuestions(self, questions_data):
        pass
    
    @abstractmethod
    def buildExam(self, examdetails):
        pass

class Level1Exam(ExamBuilder):
    def __init__(self):
        super().__init__("Week Exam", 20)
   
    def buildQuestions(self, questions_data):
        self.getExam().setQuestions(questions_data)
        
    def buildExam(self, examdetails):
        self.getExam().setExamDetails(examdetails)

class Level2Exam(ExamBuilder):
    def __init__(self):
        super().__init__("Month Exam", 40)
      
    def buildQuestions(self, questions_data):
        self.getExam().setQuestions(questions_data)
        
    def buildExam(self, examdetails):
        self.getExam().setExamDetails(examdetails)

class Level3Exam(ExamBuilder):
    def __init__(self):
        super().__init__("Final Exam", 90)
    
    def buildQuestions(self, questions_data):
        self.getExam().setQuestions(questions_data)
        
    def buildExam(self, examdetails):
        self.getExam().setExamDetails(examdetails)

class Monitor():   
    def __init__(self, builder: ExamBuilder):
        self.__builder = builder
    
    def createExam(self, examdetails, questions_data):
        self.__builder.buildQuestions(questions_data)
        self.__builder.buildExam(examdetails)
        return self.__builder.getExam().save()

if __name__ == '__main__':
    pass
    
###########################################################################3

class Repositry(metaclass=ABCMeta):
    @abstractmethod
    def getExam(self, pk:int):
        pass

class ExamsRepositry(Repositry):
    
    def getExam(self, pk:int):
        exam = Quiz.objects.get(pk=pk)
        return exam

class Proxy(Repositry):
    
    visitedExam = dict()
    
    def __init__(self):
        self.__examRepositry = ExamsRepositry()
        
    
    def getExam(self, pk:int):
        print("  ", Proxy.visitedExam)
        if pk in Proxy.visitedExam:
            
            # print("\n**From dictionary**\n")
            return Proxy.visitedExam[pk]
            
        else:
            # print("\n**From DataBase**\n")
            exam = self.__examRepositry.getExam(pk)
            Proxy.visitedExam[pk] = exam
            print(Proxy.visitedExam)
            return exam
        
    
    
    


