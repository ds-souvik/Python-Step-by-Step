"""
Args and Kwargs are an advanced type of argument.
Rule of thumb, whenever a functions is defined with a normal argument, args and kwargs, the order which should
be kept in mind as per the open source convention is:
def function(normal, *args, *kwargs)
and while calling the function also this order should be followed.
"""
#Writing a basic function which takes four arguments and directly prints them.
def fun_name_print(a,b,c,d):
    print(a,b,c,d)

fun_name_print("Souvik","Sayli","Atanu","Abhi")

#Now if we want to add one more name to this- we will have to add one more argument to the function right? For eg:

def fun_name_print1(a,b,c,d,e):
    print(a, b, c, d,e)

fun_name_print1("Souvik", "Sayli", "Atanu", "Abhi","Sushanth")

"""Now to build scalable applications where millions and billions of data is added, this is an incorrect method to use.
You cant keep on changing the number of argiments in a function every minute.
Hence args and kwargs is introduced.
Introducing Args
"""

def fun_args(normal,*args):
    print(type(args))                     #here args is passed as a tuple even if the argument is list, tuple etc
    print(args[0])
    print("***************")
    print(normal)
    for items in args:
        print(items)

list1=["Souvik","Sayli","Atanu","Abhi"]
string="This is the list of friends"
fun_args(string,*list1)
list1.append("Sushanth")                  #Appending Sushanth to the list
fun_args(string,*list1)                   #Names are getting added withput changing the functions.

"""Introducing Kwargs"""

def fun_args1(normal, *args, **kwargs):
    print(type(args))                     #here args is passed as a tuple even if the argument is list, tuple etc
    print(args[0])
    print("***************")
    print(normal)
    for items in args:
        print(items)
    for key, value in dict1.items():
        print(f"{key} is a {value}")

print("****************************************")
list2=["Souvik","Sayli","Atanu","Abhi"]
dict1={"Souvik":"Data Scientist","Sayli":"Programmer","Atanu":"M.E","Abhi":"Useless"}
string="This is the list of friends"
fun_args1(string,*list2,**dict1)
list1.append("Sushanth")                  #Appending Sushanth to the list
fun_args1(string,*list1,**dict1)                   #Names are getting added withput changing the functions.
