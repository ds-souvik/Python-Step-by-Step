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
Multiple Inheritance
"""

class Player:
    no_of_games=4

    def __init__(self,name,game):
        self.name=name
        self.game=game

    def print_details(self):
        print(f"The player's name is {self.name} and he plays these games {self.game}")

class CoolProgrammer(Employee,Player):
    #The order in which employee and player is given, is very important as per requirement.
    language="C++"
    def print_language(self):
        return self.language

souvik=Employee("Souvik",25,"Mainframe SSE")
sayli=Employee("Sayli",26,"Mulesoft SSE")
aniket=Player("Aniket",["Cricket","Chess","Volleyball"])
#harsh=CoolProgrammer("Harsh",24,"Tester")
# harsh.print_something(harsh.name)
# print(harsh.print_language())
srishti=CoolProgrammer("Srishti",26,"Tester")
print(srishti.print_language())