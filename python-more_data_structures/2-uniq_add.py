#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    seen = set()
    for num in my_list:
        if num not in seen:
            sum += num
            seen.add(num)
    return sum
