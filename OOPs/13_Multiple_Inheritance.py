class User:
    def __init__(self,name,character,exp):
        self.name=name
        self.character=character
        self.exp=exp

    def user_info(self):
        return f'{self.name} has a {self.character} with Exp. Level: {self.exp}'
        
    def sign_in(self):
        print("Logged In")

class Power1():
    def __init__(self,magic_power):
        self.magic_power=magic_power

    def check_magic_power(self,):
        return f'Magic Power: {self.magic_power}'

class Power2():
    def __init__(self,hand_power):
        self.hand_power=hand_power

    def check_hand_power(self,):
        return f'Hand Power: {self.hand_power}'

class Character(User,Power1,Power2):
    def __init__(self,name,character,exp,magic_power,hand_power):
        User.__init__(self,name,character,exp)
        Power1.__init__(self,magic_power)
        Power2.__init__(self,hand_power)

c1=Character("Priyanshu","Wizard",90,"Fire Blast","Archer")
print(c1.user_info())
print(c1.check_hand_power())
print(c1.check_magic_power())
