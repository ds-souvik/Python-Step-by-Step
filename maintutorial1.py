"""
1. Defining 2 functions here, print_name and add. Use the functions here and then import maintitorial1 in
maintutorial2. When the code will execute in maintutorial2, it will first execute whatever left is present
in maintutorial1 and then execute maintutorial2.
2. To avoid this we will have to introduce main functon in maintutorial1- What happens is that
print_name("Souvik")
false_add(11, 6)
will only execute when  maintutorial1 is executed.
3. Now outside main function if I write
print("And the name is "__name__)-- This gives the name of the .py file which is executed.
When maintutoril1 is executed, __name__=maintutorial1
When maintutorial2 is executed,__name__=maintutorial1(since it's not under main function and imported
from maintutorial1
"""

def print_name(string):
    print(f"My name is {string}")

def false_add(num1,num2):
    print(num1+num2+5)


# print_name("Souvik")
# false_add(11,6)

print("And the name is ",__name__)

if __name__ == '__main__':
    print_name("Souvik")
    false_add(11, 6)