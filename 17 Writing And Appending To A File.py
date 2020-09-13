#Syntax on how to open a new file and write text in it.
f=open("17A Souvik.txt","w")
f.write("Hello Everyone, My name is Souvik Ganguly.\n")
f.close()

#Syntax on how to open a new file, write text in it and get the number of character written.
g=open("17A Souvik.txt","w")
a=g.write("Hello Everyone, My name is Souvik Ganguly.\n")
print(a)
g.close()

#Syntax on how to open an existing file, append text in it and get the number of character written.
h=open("17A Souvik.txt","a")
b=h.write("Currently I am a mainframe developer and a stand up comic.\nI will become a data scientist in a year.")
print(b)
h.close()

#Syntax to open the file in both read and write mode.
#Benfit: So that whenever I open the file, I can do both things in a single instance.
i=open("17A Souvik.txt","r+")
i.close()
