# filter function filters out the output 

my_list=[2,5,8,9]
def multi_by_2(item):
    return item*2

def check_if_odd(item):
    return item%2 != 0

print(list(filter(check_if_odd,my_list)))

