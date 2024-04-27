# A pur function is a function that 1.give same output on a same output,2.Function should not interact or affect the outside world(outside the function).
#It's not possible to have a pure function everywhere 

def multi(list):
    new_list=[]
    for item in list:
        new_list.append(item*2)
    return new_list

print(multi([5,6,2])) 