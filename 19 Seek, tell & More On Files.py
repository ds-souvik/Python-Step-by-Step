#filepointer.tell() gives you the place value of the pointer i.e; where the pointer is.
f=open("16A souvik.txt","r")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.close()


print("*******************************************************************************************")
#filepointe.seek() places your pointer to the place value as mentioned in the argument in your file
f=open("16A souvik.txt","r")
print(f.tell())
f.seek(44)
print(f.tell())
print(f.readline())
f.close()
