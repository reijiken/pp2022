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