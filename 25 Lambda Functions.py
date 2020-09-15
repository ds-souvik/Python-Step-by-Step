# a=int(input("Enter first num: "))
# b=int(input("Enter second num: "))
#
# def add(a,b):
#     sum=a+b
#     return sum
#
# minus=lambda a,b:a-b
#
#
# print(add(a,b))
# print(minus(a,b))

def my_func(e):
    return e[1]

list1=[1,2,3,4]
list1.sort(reverse=True)
print(list1)

list2=[[1,4],[2,5],[3,6],[4,8]]
list2.sort(reverse=True,key=my_func)
print(list2)

list2.sort(key=lambda x:x[1])
print(list2)
