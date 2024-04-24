class Person:
    Gender="Male"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Person_info(self):
         print(f"{self.name} is a {self.Gender} of age {self.age}")

    @classmethod
    def change_gender(cls,update_gender):
        cls.Gender=update_gender
        print()


p1=Person("Rahul",22)
p1.Person_info()
p1.change_gender("Female")
p1.Person_info()

