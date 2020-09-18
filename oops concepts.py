"""
Here Employee is a class.
Employee() is an object and souvik and sayli are instances of objects Employee().
name,age,occupation,reviews are instance variables of instances souvik and sayli.
no_of_leaves is a class variable
"""

class Employee:
    no_of_leaves=116
    pass


souvik=Employee()
sayli=Employee()


souvik.name="Souvik"
souvik.age=25
souvik.occupation="Mainframe SSE"
souvik.reviews=["Met Expectations", "Met Expectations", "Commendable"]
print(f"Souvik has {souvik.no_of_leaves}")
print(Employee.__dict__)
print("******************************************")
Employee.no_of_leaves=120
print(f"Souvik and Sayli has {souvik.no_of_leaves and sayli.no_of_leaves} respectively")
print(Employee.__dict__)



sayli.name="Sayli"
sayli.age=26
sayli.occupation="Mulesoft SSE"

print(souvik.name,sayli.occupation, souvik.reviews)

