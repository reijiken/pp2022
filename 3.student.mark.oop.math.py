import math
import numpy as np
import curses 

Student=[]
StudentID=[]
Course=[]
CourseID=[]
Mark=[]
Credit=[]
gpa_s=[]
gpa_d=[]

D=curses.initscr()

class student:
    def __init__(self,id, name, dob,course_enter):
       self.id=id
       self.name=name
       self.dob=dob
       self.course_enter=course_enter
        
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob    


class course:
    def __init__(self,id,name,coursecredit):
        self.id=id
        self.name=name
        self.student=[]
        self.coursecredit=coursecredit

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_credit_course(self):
        return self.coursecredit


class Marks:
    def __init__(self,id_student,id_course,mark,Gpa=0):
        self.id_student = id_student
        self.id_course = id_course
        self.mark=mark
        self.Gpa=Gpa
    

    def get_id_student(self):
        return self.id_student
    def get_id_course(self):
        return self.id_course
    def get_mark(self):
        return self.mark
    def get_Gpa(self):
        return self.Gpa
    def set_Gpa(self,Gpa):
        self.Gpa=Gpa
   
def numberofstudent():
    while True:
        D.addstr("Enter the number of student in  class:")
        D.refresh()
        student_class=int(D.getstr().decode())
        if(student_class<=0):
            D.addstr("error\n")
            D.clear()
            D.refresh()
        else:
            return student_class

def add_student_infor():
    D.addstr("Enter student ID:")
    D.refresh()
    id=D.getstr().decode()

    D.addstr("Enter student name:")
    D.refresh()
    name=D.getstr().decode()

    D.addstr("Enter student dob:")
    D.refresh()
    dob=D.getstr().decode()

    st_infor=Student(id,name,dob)
    StudentID.append(id)
    Student.append(st_infor)
    D.refresh()
    D.clear()
    
def number_course():
    while True:
        D.refresh()
        D.addstr("Enter the number of course:")
        D.refresh()
        number_course=int(D.getstr().decode())
        if(number_course<=0):
            D.addstr("error\n")
            D.clear()
            D.refresh()           
        else:
            return number_course
       
def add_course():
    D.addstr("Enter the name course:")
    D.refresh()
    name=D.getstr().decode()
    
    D.addstr("Enter the ID course:")
    D.refresh()
    id=D.getstr().decode()

    D.addstr("Enter the credits are:")
    D.refresh()
    credit_course=D.getstr().decode()

    course_f=Course(name,id,credit_course)
    Course.append(course_f)
    Credit.append(credit_course)
    CourseID.append(id)
    D.refresh()
    D.clear()

def managementmark(): 
    for i in range(0,len(Student)):
        D.clear()
        D.addstr("student mark:\n")
        D.addstr("Enter the ID student:")
        id_student=D.getstr().decode()
        D.refresh()
        if id_student in StudentID:
            for j in range(0,len(Course)):
                D.addstr("Enter the ID course:")
                id_course= D.getstr().decode()
                D.refresh()
                if id_course in CourseID:
                    D.addstr("Enter the mark of student:")
                    mark=math.floor(float(D.getstr().decode()))
                    D.refresh()
                    if (mark<0) or (mark>20):
                        try:
                            D.addstr("Faild\n")
                        except curses.error:
                           pass
                        D.clear()
                        D.refresh()
                        D.addstr("Try again\n")
                        mark=math.floor(float(D.getstr().decode()))
                   
                else:
                    exit()
        else:
            exit()                

    infor_mark=Marks(id_student,id_course,mark)
    Mark.append(infor_mark)
    gpa_d.append(mark)
 

def aver_gpa():
    var=np.array([gpa_d])
    cred=np.array([Credit])
    D.addstr("Name of the student that you want to calculate GPA:")
    name =D.getstr().decode()
    if name in Student:
        for i in range(len(Mark)):
            recallcre=np.sum(cred)
            recallvar=np.sum(np.multiply(var,cred))
            D.refresh()
            Gpa=recallvar/recallcre
            D.refresh()                
    else: 
        return 0

    gpa_s.append(Gpa)
    D.refresh()

    for st_infor in Mark:
        D.clear()
        D.refresh()
        D.addstr(" Mark_studentid: %s   Gpa:%s \n" %(st_infor.get_id_course(), Gpa))
        D.refresh()

        break

def show_student():
    D.addstr("student list:\n")
    D.refresh()
    for Students in Student:
        D.addstr("[ID-student: ] %s   [Name-student: ] %s    [DoB_Student: ] %s\n" % (Students.get_id(),Students.get_name(),Students.get_dob()))
        D.refresh()

def show_course():
    D.addstr("course list\n")
    D.refresh()
    for Courses in Course:
        D.addstr("[ID-COurses]: %s    [Name-Course]: %s      [Credit-Course]: %s\n"%(Courses.get_id(),Courses.get_name(),Courses.get_credit_course()))
        D.refresh()

def show_mark():
    D.addstr("mark\n")
    D.refresh()
    for Marks in Mark:
        D.addstr("[ID-course]: %s      [ID-Student]: %s       [mark]: %s\n"%(Marks.get_id_course(),Marks.get_id_course(),Marks.get_mark()))
        D.refresh()

def GPA_decending():
    arrr=np.array([gpa_s])
    arrr[::-1].sort()
    D.addstr("The list is %s: \n"%(arrr))
    D.refresh()

s=int(numberofstudent())
for i in range(0,s):
    add_student_infor()
show_student()

c=int(number_course())
for i in range(0,c):
    add_course()
show_course()

managementmark()

aver_gpa()

D.refresh()
D.clear()

D.addstr("your choice\n")
D.addstr("1.check student mark")
D.addstr("2.no\n")
       
a = int(D.getstr().decode())
if a == 1:
    D.clear()
    D.addstr("This is student mark:\n")
    D.refresh()
    D.clear()
    curses.napms(1500)
    show_mark()
    D.addstr("This is student GPA:\n")
    D.refresh()
    curses.napms(1500)
    GPA_decending()
else:
    D.addstr("end")
    curses.napms(1500)
    curses.endwin()
