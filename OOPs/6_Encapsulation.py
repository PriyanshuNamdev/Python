class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print( f"{self.name} is {self.age} years old")
    
p1=Person("Priyanshu",20)
p1.info()