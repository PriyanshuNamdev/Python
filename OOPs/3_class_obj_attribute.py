class Player:
    membership="Player have membership"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print(f"{self.name} is {self.age} years old and he likes to do running")

p1=Player("Priyanshu",20)
print (p1.membership)
# All object have access to it .

p2=Player("Tushar",21)
print (p2.membership)

