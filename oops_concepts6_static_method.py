"""
When we have to execute something without a self(instance variable) or a class variable, we can use static method.
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

    #When we have to execute something without a self(instance variable) or a class variable, we can use static method
    @staticmethod
    def print_something(string1):
        print(f"{string1} is a good boy")




souvik=Employee("Souvik",25,"Mainframe SSE")
sayli=Employee("Sayli",26,"Mulesoft SSE")
souvik.print_something(souvik.name)
#We can also call the static methodusing class(Employee)
Employee.print_something(souvik.name)
