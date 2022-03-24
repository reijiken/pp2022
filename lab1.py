def s ():
    return int (input ("Enter number of students: "))
    
def d ():
    return int (input ("Enter number of courses: "))
    
def e ():
    cid = input ("Enter course id: ")
    cname = input ("Enter course name: ")
    return cid, cname
    
def h ():
    sid = input ("Enter student id: ")
    sname = input ("Enter student name: ")
    sdob = input ("Enter student's dob: ")
    return sid, sname, sdob 
    
def m (sid, cid):
    prompt = f"Enter marks for student {sid} for course {cid}: ".format (sid, cid)
    input (prompt)
    
nStudents = s ()
studentLst = []
for i in range (nStudents):
    sid, nm, dob = d ()
    studentLst.append ((sid, nm, dob))

nCourses = e ()
courseLst = []
for i in range (nCourses):
    cid, cname = h ()
    courseLst.append ((cid, cname))
    
p = {}    
n = int (input ("Enter how many student-course marks do you want to enter? "))
for i in range (n):
    while True:
        sid = input ("Enter student id: ")
        cid = input ("Enter course id: ")
        if sid not in [student [0] for student in studentLst]:
            print ("Bad student id")
            continue 
        if cid not in [course [0] for course in courseLst]:
            print ("Bad course id")
            continue 
        break
    marks = int (input ("Enter marks: "))
    if cid in p:
        p [cid].append ((sid, marks))
    else:
        p [cid] = [(sid, marks)]
        
print ("\nListing all students now..")
for s in studentLst:
    print (f"Student id: {s[0]} Name: {s[1]} Dob: {s[2]}")

print ("\nListing all courses now..")
for c in courseLst:
    print (f"Course id: {c[0]} Name: {c[1]}")
    
cid = input ("\nWhich course do you want to see all student marks for? ")
if cid in p:
    for tups in d [cid]:
        print (f"Student {tups[0]} got {tups [1]} marks")