Course=[]
CourseID=[]
Credit=[]
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