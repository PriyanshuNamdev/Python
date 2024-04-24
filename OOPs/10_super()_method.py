#super() method is used to call the init function of the parent class inside the functions of child class

class User:
    def __init__(self,gender):
        self.gender=gender
        print("Living being")

class Person1(User):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # super().__init__(gender)

    def Person_info(self):
        super().__init__(gender)
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

gender="male"
p1=Person1("Priyanshu",20)
p1.Person_info()