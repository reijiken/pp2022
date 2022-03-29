Student=[]
StudentID=[]
Course=[]
CourseID=[]
class course:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.student=[]

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name

class student:
    def __init__(self,id, name, dob,course_enter,mark):
       self.id=id
       self.name=name
       self.dob=dob
       self.course_enter=course_enter
       self.mark=mark

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob  
         
def number_course():
    number_course=int(input("Enter the number of course:"))
    if(number_course<=0):
        print("error")
        return 0
    else:
        return number_course
        
def add_course():
    name=input("Enter the name course:")
    id=input("Enten the ID course: ")
    course_f={
        'name':name,
        'id':id
    }
    Course.append(course_f)
    CourseID.append(id)        
    
def inputstudent():
    student_class=int(input("Enter the number of student in class:"))
    if(student_class<=0):
        print("error")
        return 'False'
    else:
        return student_class

def add_student_infor():
    print("enter information of student:")
    
    id=input("Enter the ID:")
    name=input("Enter the student name:")
    dob=input("Enter the dob student:")
    course_enter=input("Enter the id course that student in:")
    mark=input("Enter student mark:")
    st_infor={
        'id':id,
        'name':name,
        'dob':dob,
        'course_enter':course_enter,
        'mark':mark
    }
    StudentID.append(id)
    Student.append(st_infor)

def show_course():
    print("course list")
    for i in range(0,len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")

def show_student():
    print("Student list ")
    for i in range(0,len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']} Courseid:{Student[i]['course_enter']} Mark:{Student[i]['mark']}")

j=int(number_course())
m=1
while m<=j:
    m+=1
    add_course()
show_course()

b=int(inputstudent())
z=1
while z<=b: 
    z+=1
    add_student_infor()
show_student()




