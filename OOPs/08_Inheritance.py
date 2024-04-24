class User:
    def loge_in(self):
        print("Logged In")

class Account_1(User):
    def __init__(self,name,password):
        self.name=name
        self.password=password

    def Info(self):
        print(f"Name: {self.name} Password: {self.password}")


class Account_2(User):
     def __init__(self,name,password):
        self.name=name
        self.password=password

     def Info2(self):
        print(f"Name: {self.name} Password: {self.password}")

u1=User()
u1.loge_in()
u2=Account_1("Priyanshu",852654)
u2.Info()
u2.loge_in()
u3=Account_2("Raghav",951357)
u3.Info2()
u3.loge_in()