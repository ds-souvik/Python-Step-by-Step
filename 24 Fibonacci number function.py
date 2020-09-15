number=int(input("Enter the nth number: "))

def fibonacci_iterative(n):
    list1=[0,1]
    if (n<=2):
        return list1[n-1]
    else:
        while(len(list1)!=n):
            length= len(list1)
            list1.append(list1[length-2]+list1[length-1])
        return list1[n-1]

list2=[0,1]
def fibonacci_recursive(n):

    if (len(list2)==n):
        return list2[n-1]
    else:
        length=len(list2)
        list2.append(list2[length-2]+list2[length-1])
        return fibonacci_recursive(n)


def fib_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)

print(fibonacci_iterative(number))
print(fibonacci_recursive(number))
print(fib_recursive(number))

