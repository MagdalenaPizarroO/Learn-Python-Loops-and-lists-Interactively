my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:

def maxInteger(list):
    biggest_integer = 0
    for num in list:
        if num > biggest_integer:
            biggest_integer = num
    return biggest_integer

print(maxInteger(my_list))