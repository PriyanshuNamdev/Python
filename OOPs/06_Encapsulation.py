#Encapsulation can be describe as wrapping up of data and methods that use the data in a single unit.
class Person:                              #                                 -----
    def __init__(self,name,age):           #                                     !   wrapping            
        self.name=name                     #                                     !    up data
        self.age=age                       #                                 -----           

    def info(self):
        print( f"{self.name} is {self.age} years old")
    
p1=Person("Priyanshu",20)
p1.info()