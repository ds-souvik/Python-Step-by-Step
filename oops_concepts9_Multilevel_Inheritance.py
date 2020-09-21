class Dad:
    history_knowledge="Expert"

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