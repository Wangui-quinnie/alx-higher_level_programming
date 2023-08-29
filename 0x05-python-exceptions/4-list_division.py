#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            element1 = my_list_1[i]
            element2 = my_list_2[i]
            result = element1 / element2
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except (TypeError, ValueError):
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)

    return new_list
