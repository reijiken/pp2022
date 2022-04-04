import math
import numpy as np
import curses 
from domain.student import *
from domain.course import *
from domain.mark import*
D=curses.initscr()
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