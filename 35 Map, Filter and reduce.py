list2=["11","22","33","21"]
"""
Now to convert the above elements of list2 into int,the below for-loop needs to be written
for i in range(len(list2)):
    list2[i]=int(list2[i])
    
But instead of this for-loop, I can use map function to do the same task.
"""
list2= list(map(int, list2))
print(list2)
list2[2]+=5
print(list2)

def fun_sq(a):
    return a*a
num_list=[1,2,3,4,5,6,7,8,9,10]
sq_list_of_num=list(map(fun_sq, num_list))
sq_list_of_num1=list(map(lambda x: x * x, num_list))
print(sq_list_of_num)
print(sq_list_of_num1)

def square(b):
    return b*b

def cube(c):
    return c*c*c

func=[square,cube]

for i in range(5):
    print(list(map(lambda x:x(i), func)))

"""**************************************FILTER********************************
"""
"""To filter elements from the list which are greater than 5"""
numbers=[1,2,3,4,5,6,7,8,9,10]
numbers2=[]
numbers3=[]
def greater_than_5(num):
        return num>5
for i in range(len(numbers)):
    e = greater_than_5(numbers[i-1])
    if e==True:
        numbers2.append(numbers[i-1])
    else:
        continue
numbers2.sort()
print(numbers2)

"""Similar thing can be done using filters"""
numbers3=list(filter(greater_than_5, numbers))
print(numbers3)


"""**************************************REDUCE********************************
"""
"""I want to add all the elements and get it's sum"""
#Without filters
list3=[1,2,3,4]
sum=0
for i in list3:
    sum+=i
print(sum)

#With reduce
from functools import reduce

sum1=reduce(lambda x,y:x+y, list3)
print(sum1)