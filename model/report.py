from abc import ABCMeta, abstractmethod

from employee import Employee,  Teacher, Student

# Builder Design Pattern

class Report():

    def __init__(self):
        self.__topic = ""
        self.__date = ""
        self.__report = ""
    
    def setTopic(self, topic):
        self.__topic = topic

    def setReport(self, report):
        self.__report = report
    
    def setDate(self, date):
        self.__date = date
    
    def __str__(self):
        return f'topic: {self.__topic}, Report: {self.__report} made in Date: {self.__date}'


class ReportBuilder(metaclass=ABCMeta):

    def __init__(self):
        self.report = Report()
    
    @abstractmethod
    def buildTopic(self):
        pass

    @abstractmethod
    def buildReport(self, employee):
        pass

    @abstractmethod
    def buildDate(self):
        pass

    def getReport(self):
        return self.report


class StudentReportBuilder(ReportBuilder):

    def buildTopic(self):
        self.report.setTopic('Student Report')
    
    def buildReport(self, employee:Employee):
        self.report.setReport(f'this Stuent name is {employee.getName()}, at Level {employee.getLevel()}')
    
    def buildDate(self):
        self.report.setDate(f'now')
  

class TeacherReportBuilder(ReportBuilder):

    def buildTopic(self):
        self.report.setTopic('Teacher Report')
    
    def buildReport(self, employee:Employee):
        self.report.setReport(f'this Stuent name is {employee.getName()}, at Level {employee.getSalary()}')
    
    def buildDate(self):
        self.report.setDate(f'now')


class GenerateReport: # like Cacher

    def __init__(self, builder:ReportBuilder, employee:Employee):
        self.__builder = builder
        self.__employee = employee

    
    def generate(self):
        self.__builder.buildTopic()
        self.__builder.buildReport(self.__employee)
        self.__builder.buildDate()

        return self.__builder.getReport()


if __name__ == '__main__':
    
    teacher = Teacher('Ahmed Amer', 'ahmed@gmail.com', '01099401398', '123', 10000, 'teacher')
    teacherReportBuilder = TeacherReportBuilder()

    student = Student('Ahmed Amer', 'ahmed@gmail.com', '01099401398', '123', 4)
    studentReportBuilder = StudentReportBuilder()

    report = GenerateReport(studentReportBuilder, student).generate()
    
    print(report)

