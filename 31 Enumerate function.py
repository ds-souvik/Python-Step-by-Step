"""You have a list list1 which has list of vegetbles"""
list1=["Potato", "Onion", "Tomato", "Papaya"]

""" Now you come to know that your dad had brought all the items in the even place yesterday and you don't need 
it this time
"""

#Without enumerate:
i=0
for items in list1:
    if i%2==0:
        print(f"Jarvis please bring {list1[i]}")
    i+=1

print("*********************************************")
#using enumerate function:
for index,item in enumerate(list1):
    if index%2==0:
        print(f"Jarvis please bring {item}")
