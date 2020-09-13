"""Why with open is used instead of open and close?
While using with open, you don't have to worry abput closing the file as it automatically closes it once the program
is out of with open block.
Also all read write functions can be performed under the same.
"""

with open("16A souvik.txt") as f:
    a=f.readlines()
    print(a)

#If the flie is not closed after control comes out of with open block, the below code will give error
f=open("16A souvik.txt","rt")
a=f.readlines()
print(a)
f.close()