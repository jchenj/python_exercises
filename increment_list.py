"""
Write & test a function that increments each element of a list by 1
"""

my_list = [-3, 0, 5]


def increment_list1(l):
    new_list = []
    for elem in l:
        elem = elem + 1
        new_list.append(elem)
    l = new_list
    print(l)


increment_list1(my_list)


def increment_list2(l):
    for i in range(len(l)):
        l[i] = l[i] + 1
    print(l)


increment_list2(my_list)