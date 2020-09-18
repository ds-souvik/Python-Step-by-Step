class Employee:
    no_of_leaves=116

    def print_info(self):
        print(f"Name is {self.name}. Age is {self.age} and occupation is {self.occupation}")

souvik=Employee()
sayli=Employee()

souvik.name="Souvik"
souvik.age=25
souvik.occupation="Mainframe SSE"

sayli.name="Sayli"
sayli.age=26
sayli.occupation="Mulesoft SSE"

souvik.print_info()
sayli.print_info()

print(souvik.no_of_leaves)