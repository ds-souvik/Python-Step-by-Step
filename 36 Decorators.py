"""
When is decorator used?
When you have to use a single function 10 times, you kind of make a blue-print of the function and then
use it as a decorator everywhere.
"""

def function1():
    print("Hey there! My name is Souvik Ganguly")
"""I have defined a function function1 above which is printing a string.
Now if I assign function1 to function2 and then delete function1... will I get anything while executing function2?
Answer is yes- Because there is already a copy if function 2 made"""
function2=function1
del function1
function2()

################################################################################################
"""Now we will learn returning a function within a function"""
def function3(num):
    if num==0:
        return print
    elif num==1:
        return sum

print(function3(1))
"""So now <built-in function print> and <built-in function sum> are returned as per num"""

################################################################################################
"""Now we will learn passing a function as an argument to a different function"""
def function4(func):
    func("Hey Hey!! We have learnt how to pass a function as an argument to a different function")

function4(print)


print("************************************************************************************")
################################################################################################
"""Now let's see why decorators are needed"""

def function5(other_func):
    def inside_function():
        print("Other function will be executed")
        other_func()
        print("Other function executed")
    return inside_function

def who_am_I():
    print("I am Souvik Yo!")

who_am_I=function5(who_am_I)
who_am_I()
"""Now here to shorten this process of calling a function as an argument within a function, we can use decorators"""
print("*******************************************************************************************")
@function5
def who_am_I_dec():
    print("I am Souvik Yo!")

#who_am_I=function5(who_am_I)
who_am_I_dec()

