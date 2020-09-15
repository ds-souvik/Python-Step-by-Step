var1=20

print("Before calling any func", var1)
def fun1():
    var1=10
    print("When func1 executes",var1)
    def func2():          #This is nested function
        global var1
        var1=30
        print("When func2 executes",var1)
    func2()

fun1()
print("When all the functions are executed",var1)