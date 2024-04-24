class Superlist(list):
    def __len__(self):
        return 1000
    
super_list1=Superlist()
print(len(super_list1))
super_list1.append("Delloit")
super_list1.append("Google")
super_list1.append("Apple")
super_list1.append("Microsoft")
print(super_list1[2])