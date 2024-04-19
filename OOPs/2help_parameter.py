class Player:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print(f"{self.name} is {self.age} years old and he likes to do running")

help(Player)
# It give the complete blueprint of the class