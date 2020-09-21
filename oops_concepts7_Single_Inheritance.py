"""
Inheritance: You have 2 classes where the parent class:Employee has a basic template.
Now you wrote another class Programmer.
Now a programmer is also an employee but it has some additional qualities/features etc.
Keeping in mind the best coding practice DRY:DO NOT REPEAT, since there is a template similarity between
Employee class and Programmer class I don't want to repeat the code patch of Employee in Programmer.
Hence I am inheriting properties of class Employee in Programmer.
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

"""
Single Inheritance
"""
class Programmer(Employee):
    def __init__(self,aname,aage,arole,salary,*languages):
        self.name=aname
        self.age=aage
        self.occupation=arole
#Now here we could have used the constructore of the super class by using super() to follow the code-reusability
#concept. But for now we have copied the constructor.
        self.salary=salary
        self.languages=languages

    def print_from_new_class(self):
        print(f"My name is {self.name}. I am {self.age} years old. My role is {self.occupation}. My salary is {self.salary}."
              f"He knows {self.languages}")





souvik=Employee("Souvik",25,"Mainframe SSE")
sayli=Employee("Sayli",26,"Mulesoft SSE")
souvik.print_something(souvik.name)
#We can also call the static methodusing class(Employee)
Employee.print_something(sayli.name)


"""Now making an instance of a subclass(Programmer) and executing it's function"""
atanu=Programmer("Atanu",26,"Clerk",10000,*["C++","Python","JAVA"])
atanu.print_from_new_class()
