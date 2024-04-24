from typing import Any


class Toy:
    def __init__(self,color,age):
        self.color=color
        self.age=age
        self.my_dict={
            "Name":"BumbleBee",
            "Weight":50
            }
        
    def __str__(self):
        return f"{self.age}"
    
    def __len__(self):
        return 8
    
    def __call__(self):
        print("Yess!!!!")

    def __getitem__(self,i):
        return self.my_dict[i]
    
t1=Toy("Yellow",2)
print(t1.__str__())
print(str(t1))
print(len(t1))
print(t1['Name'])