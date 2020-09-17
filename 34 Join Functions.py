list1=["Souvik","Sayli","Atanu","Abhi"]

string="The members of the group are"
for items in list1:
    if items==list1[len(list1)-1]:
        string=string+" "+items
    else:
        string=string+" "+items+ " "+ "and"

print(string)

for i in list1:
    print(i,"and",end=" ")
print("\n")

"""Instead of using these 2 ways, we can use a simple join function here"""
a=" and ".join(list1)
print(a)

