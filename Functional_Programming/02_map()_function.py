def multi_by_2(item):
    return item*2

print(list(map(multi_by_2,[2,5,8])))



#To check that it does not affect the code outside the function-

my_list=[2,5,8]
def multi_by_2(item):
    return item*2

print(list(map(multi_by_2,my_list)))
print(my_list)

#as we can see that my_list does not change because the map function create a whole new list in other memory space