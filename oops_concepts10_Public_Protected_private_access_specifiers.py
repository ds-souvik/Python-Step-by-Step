class Dad:
    history_knowledge="Expert"  #This is a public variable
    _person="Good"              #This is a protected variable
    __property="Nothing"        #This is a private variable.

    def print_dad_details(self):
        print(f"Madan Mohan Ganguly had {self.history_knowledge} level of knowledge in history")

class Son(Dad):
    hard_work_grade="Expert"
    history_knowledge = "Dope Expert"
    def print_son_details(self):
        print(f"Debdas Ganguly did {self.hard_work_grade} level of hardwork")

class Grandson(Son):
    intelligence="good"
    def print_grandson_details(self):
        print(f"Souvik Ganguly had {self.intelligence} level of intelligence")

souvik=Grandson()
debdas=Son()
madan=Dad()

madan.print_dad_details()
souvik.print_dad_details()
debdas.print_dad_details()
souvik.print_dad_details()
souvik.print_son_details()
debdas.print_son_details()
souvik.print_grandson_details()
print(madan.history_knowledge)      #Public variables can be used anywhere
print(madan._person)                #Protected variables can be used withing the class and the sub-classes.
print(madan._Dad__property)         #Private variables cannot anywhere. Even though with name angling it can be used within
                                    #the sub classes.
print(debdas._person)
print(debdas._Dad__property)