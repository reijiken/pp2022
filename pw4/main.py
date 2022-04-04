import math
import numpy as np
import curses 
from domain.student import *
from domain.course import *
from domain.mark import*
D=curses.initscr()
from input import number_course,numberofstudent,add_course,add_student_infor,mark_mana,aver_gpa
from output import GPA_decending,show_course,show_student,show_mark
class main():
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

D.addstr(0,5,"""your choice\n""")
D.addstr(1,5,"1.check student mark")
D.addstr(2,5,"2.no\n")
       
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
