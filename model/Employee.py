from abc import ABCMeta, abstractmethod
# from django.contrib.auth.models import User

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



class Teacher(Employee):
    
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
class Principle(Teacher, object):

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
        pass

class Student(Employee):
    
    def __init__(self, name, email, phone, password, level):
        super().__init__(name, email, phone, password)
        self.__level = level

    def getLevel(self):
        return self.__level
    
    def setLevel(self, level):
        self.__level = level

        
