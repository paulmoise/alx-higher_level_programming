#!/usr/bin/python3


def list_division(my_list1, my_list2, list_length):
    """
    Function that divides element by element 2 lists.
    """
    arr = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list1[i]/my_list2[i]
        except (TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            arr.append(res)
    return arr
