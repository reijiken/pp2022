import numpy as np
import curses 
from domain.student import *
from domain.course import *
from domain.mark import*
D=curses.initscr()
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