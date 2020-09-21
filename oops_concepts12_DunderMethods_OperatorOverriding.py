"""
The methods that starts with '__' and ends with '__' are called dunder methods.
__init__ is called a dunder init and it's a special method since it's a constructor
"""
class Employee:
    no_of_leaves=116

    def __init__(self,aname,aage,arole):
#Here aname,aage and arole are the ergume nts of the constructor
#name,age and occupation are the instance variables"""
        self.name=aname
        self.age=aage
        self.occupation=arole

    def print_details(self):
        return (f"{self.name}'s age is {self.age} and occupation is {self.occupation}.")

    @classmethod
    def change_no_of_leaves(cls,changed_leaves):
        cls.no_of_leaves=changed_leaves

    #dunder methods
    def __add__(self, other):
        return self.age+ other.age

    def __truediv__(self, other):
        return self.age/other.age

    """Usually __repr__ is used to define an instance of a class with all the values of instance variables/arguments
    of constructors"""
    def __repr__(self):
        return f"Employee('{self.name}',{self.age},'{self.occupation}')"

    def __str__(self):
        return (f"{self.name}'s age is {self.age} and occupation is {self.occupation}.")


souvik=Employee("Souvik",25,"Programmer")
bittu=Employee("Bittu",29,"Delivery Boy")
print(souvik+bittu)
"""The above print without a dunder method will give an error:
TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
Now introducing a dunder method to add ages of both the objects whenever objects are added
"""
print(bittu/souvik)
"""
Now priority of __repr__ and __str__
if only repr is present printing the object gives repr
if only str is present printing the object gives str
when both of them are present, result will always have str.
When both of them are present, repre will only execute if it's explicitly given repr(object) 

"""
print(bittu)
print(str(souvik))
print(repr(souvik))