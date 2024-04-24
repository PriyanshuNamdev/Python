#Polymorphism refers to the ability of different objects to share the same method or function name, but with different implementations.

class Player:
    def __init__(self):
        pass
    def Exp(self):
        print("None")

class Player1(Player):
    def __init__(self,name,character):
        self.name=name
        self.character=character

    def Exp(self,exp_lvl=0):
        self.exp_lvl=exp_lvl
        print(f"Player {self.name} has a {self.character} of Exp level: {self.exp_lvl}")
    
p1=Player1("Priyanshu","Wizard")
p1.Exp(50)



        