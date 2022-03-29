class student:
    def __init__(self,id, name, dob,mark):
       self.id=id
       self.name=name
       self.dob=dob
       self.mark=mark
    def display(self, d):
            print("Name   : ", d.name)
            print("RollNo : ", d.id)
            print("Date of birth : ", d.dob)
            print("Marks : ", d.mark)
            print("\n")
    def accept(self, id, name, mark,dob ):
        d = student(id, name, mark,dob)
        lst.append(d)
    def search(self, a):
        for i in range(lst.__len__()):
            if(lst[i].id == a):
                return i       
                                  
    def delete(self, a):
        i = obj.search(a)  
        del lst[i]
  
    def update(self, a, New):
        i = obj.search(a)
        id = New
        lst[i].id = id
          
class course:
    def __init__(self,name,last_student):
        self.name=name
        self.last_student=last_student
        self.student=[]

    def input_student(self,student):
        if len(self.student)<self.last_student:
            self.student.append(student)
            return True
        return False
    
lst=[]
obj = student( 0,'', 0,0)
print("enter id,name and mark ")
obj.accept( 1,"D",30_10, 100)
obj.accept( 2,"E",9_8, 90)
obj.accept( 3,"F",10_6, 80) 

print("\n")
print("\nList of Students\n")
for i in range(lst.__len__()):    
    obj.display(lst[i])

print("\n Student Found, ")
s = obj.search(2)
obj.display(lst[s])

obj.delete(2)
print(lst.__len__())
print("List after deletion")
for i in range(lst.__len__()):    
    obj.display(lst[i])

obj.update(3, 2)
print(lst.__len__())
print("List after updation")
for i in range(lst.__len__()):    
    obj.display(lst[i])



