#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list1 = []
    for i in my_list:
        if i == search:
            my_list1.append(replace)
        else:
            my_list1.append(i)
    return my_list1
