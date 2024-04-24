class Player:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print(f"{self.name} is {self.age} years old and he likes to do running")

p1=Player("Priyanshu",20)
p1.run()