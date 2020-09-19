"""Here I dont want to pass values of my instance variables again and again while defining an instance
in a constructor format. I want to pass the entire thing as a string like:
"Atanu-26-Clerk" and define an instance.

"""

class Employee:
    no_of_leaves=116

    def __init__(self,aname,aage,arole):
#Here aname,aage and arole are the ergume nts of the constructor
#name,age and occupation are the instance variables"""
        self.name=aname
        self.age=aage
        self.occupation=arole

    @classmethod
    def change_no_of_leaves(cls,changed_leaves):
        cls.no_of_leaves=changed_leaves

    @classmethod
    def value_instance_arg(cls,string):
        # value_list=string.split("-")
        # return cls(value_list[0],value_list[1],value_list[2])
        return cls(*string.split("-"))




souvik=Employee("Souvik",25,"Mainframe SSE")
sayli=Employee("Sayli",26,"Mulesoft SSE")
print(souvik.no_of_leaves)
print(sayli.no_of_leaves)
souvik.change_no_of_leaves(120)
print(souvik.no_of_leaves)
print(sayli.no_of_leaves)
# souvik.change_print_info("Souvik",25,"Mainframe SSE",souvik.no_of_leaves)
atanu=Employee.value_instance_arg("Atanu-25-Clerk")

"""Something new that we got from this code"""
print("****************************************************")
print(atanu.occupation)