#Abstraction can be defined as hidding up all the unnecessory details and only showing which is needed

class Person:                             
    def __init__(self,name,age):                  
        self.name=name                     
        self.age=age                                

    def info(self):
        print( f"{self.name} is {self.age} years old")
    
p1=Person("Priyanshu",20)
p1.info() # here if we only need to see how method is calling we don't need to see what is happening inside the info function