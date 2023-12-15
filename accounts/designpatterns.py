
from abc import ABCMeta, abstractmethod
from . models import Student
from . models import Notification as Note

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



# ###############################################################################

# Factory 

class Notification(metaclass=ABCMeta):
    
    def __init__(self):
        self.__message = ""
        self.__level = 1
        
    def setMessage(self, message):
        self.__message = message

    def setLevel(self, level):
        self.__level = level
    
    def getMessage(self):
        return self.__message
    
    def getLevel(self):
        return self.__level
    
    @abstractmethod
    def send(self):
        pass
    
class SMSNotification(Notification):
    
    def send(self):
        print("send by sms")
    
    
class WhatsAppNotification(Notification):
             
    def send(self):
        print("send by whatapp")
    
class WebsiteNotification(Notification):

    def send(self):
        print("Hellow web")
        students = Student.objects.filter(level=self.getLevel())
        for stude  in students:
            noti = Note(student=stude, message=self.getMessage())
            noti.save()
    


class Factor:
    
    def sendNotification(self, notificationType) -> Notification:
        
        if notificationType == 'whatsapp':
            return WhatsAppNotification()
        elif notificationType == 'sms':
            return SMSNotification()
        else:
            return WebsiteNotification()
        

if __name__ == '__main__':
    factor = Factor()
    notification = factor.sendNotification('web')
    notification.send()
    