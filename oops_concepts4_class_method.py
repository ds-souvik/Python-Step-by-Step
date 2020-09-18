class Employee:
    no_of_leaves=116

    def __init__(self,aname,aage,arole):
#Here aname,aage and arole are the ergume nts of the constructor
#name,age and occupation are the instance variables"""
        self.name=aname
        self.age=aage
        self.occupation=arole


    def print_info(self):
        print(f"Name is {self.name}. Age is {self.age} and occupation is {self.occupation}")

    @classmethod
    def change_no_of_leaves(cls,changed_leaves):
        cls.no_of_leaves=changed_leaves


souvik=Employee("Souvik",25,"Mainframe SSE")
sayli=Employee("Sayli",26,"Mulesoft SSE")
print(souvik.no_of_leaves)
print(sayli.no_of_leaves)
souvik.change_no_of_leaves(120)
print(souvik.no_of_leaves)
print(sayli.no_of_leaves)
# souvik.change_print_info("Souvik",25,"Mainframe SSE",souvik.no_of_leaves)