#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except (ZeroDivisionError):
            print('division by 0')
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            results.append(result)
    return results
