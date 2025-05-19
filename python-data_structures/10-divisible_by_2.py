#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in my_list:
        new_list.append(n % 2 == 0)
    return new_list
