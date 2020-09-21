class A:
    classvar1="I'm a variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="This is class A'S instance variable classvar1"
        self.special="special"

class B(A):
    classvar1 = "I'm a variable in Class B"
    def __init__(self):
        super().__init__()
        self.var1="I am inside class B's constructor"
        self.classvar1="This is class B'S instance variable classvar1"
        #super().__init__()


a=A()
b=B()
print(a.classvar1)
print(b.classvar1)
print(b.special)
print(b.classvar1)
"""1. Commenting classvar1 in class B, print(b.classvar1) will give "I'm a variable in class A"
"""

"""2. Uncommenting classvar1 in class B and making an instance variable classvar1 inside constructor of class B.
b.classvar1 gives 'This is class B'S instance variable classvar1': priority instance variable>class variable
a.classvar1 gives 'I'm a variable in class A' : In class A only class variable is present
"""

"""3. Commenting instance variable classvar1 from constructor of class B and making a new instance variable 
inside constructor od class B as:
self.classvar1="This is class A'S instance variable classvar1"

a.classvar1 will give 'This is class A'S instance variable classvar1': priority instance variable>class variable

b.classvar1 will give 'I'm a variable in Class B'. Here ideally instance variable classvar1 of class A should have 
executed as per priority but it didn't execute since the constructor if class A was over-riden in class B and the
previous version of an overriden constructor is never executed. To execute the class A constructor so that as per
priority b.classvar1 gives 'This is class A'S instance variable classvar1' we will have to introduce
super() class  
"""



