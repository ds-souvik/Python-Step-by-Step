#open("16A souvik.txt")    #Syntax to pen a file.

f= open("16A souvik.txt")  #Here f is a file pointer
content1=f.read()
print("The content of the file is:")
print(content1)
f.close()


g= open("16A souvik.txt","r")  #Here g is a file pointer
# #here "r" is the mode, It can also be rb-binary, rt-text(this one is the default)
content2=g.read()
print("The content of the file is:")
print(content2)
g.close()

h= open("16A souvik.txt")  #Here h is a file pointer
content=h.read(3)          #This will read the first 3 bytes.
print("The content of the file is:")
print("1",content)
print("2",h.read(4))
#Since the first 3 bytes were already read in the same open-close instance, it will read the 4-7 bytes here.
h.close()

i= open("16A souvik.txt")  #Here i is a file pointer
content=i.read(399)          #Since the file doen't have 399 bytes, it will read the available bytes in the file.
print("The content of the file is:")
print("1",content)
print("2",i.read(4))
#Since all the bytes were already read in the same open-close instance, it won't return anything from the file.
i.close()

#To read the file character by character.
print("**************************************************************")
j= open("16A souvik.txt")  #Here j is a file pointer
content=j.read()
print("The content of the file line-by-line is:")
for line in content:
    print(line)
j.close()


#1st method To read the file line by line.
print("**************************************************************")
k= open("16A souvik.txt")  #Here k is a file pointer

#content=k.read()
"""content cannot read the file meaning one k.read is executed, the file pointer k is empty.
So if it's iterated second time it's of no use."""

print("The content of the file line-by-line is:")
for line in k:
    print(line,end="")
j.close()

#2nd method To read the file line by line.
print("\n**************************************************************")
l= open("16A souvik.txt")  #Here l is a file pointer
print("The content of the file line-by-line using readline is: ")
print(l.readline(),end="")
print(l.readline(),end="")
print(l.readline(),end="")
l.close()

#To read the lines of the file in a list:
print("\n**************************************************************")
m= open("16A souvik.txt")  #Here m is a file pointer
print("The content of the file line by line in a list is: ")
print(m.readlines())
m.close()

