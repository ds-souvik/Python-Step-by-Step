import time

""" Let's compare the time taken to execute a for-loop and a while-loop for the same actions using 
time in-built module and time.time() funtion
"""

# initial_time=time.time()
# #print(initial_time)
#
# for i in range(200):
#     print(f"{i}. Executing for loop")
# print(f"Time taken for for-loop is {((time.time())-initial_time)}")
#
# time_after_for=time.time()
# j=0
# while(j<=200):
#     print(f"{j}. Executing while loop")
#     j+=1
# print(f"Time taken for while-loop is {((time.time())-time_after_for)}")

"""How to display current time in a standard fashion using time.localtime() and time.asctime()"""
t=time.localtime()
print(t)
print(time.asctime(t))
print("****************OR**************")
print(time.asctime(time.localtime()))

"""time.sleep(arg): To make the program wait for some time before execution. arg passed here is seconds you want
the program to wait."""
for i in range(5):
    time.sleep(2)
    print("Let's see the magic of sleep function in time module")

