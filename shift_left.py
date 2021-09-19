#the program prints the new list of the user when the first item moving to the last on the list.

def shift_left(my_list):
    """the func receives a list, replace the items on the list with the item on the left
    :param my_list: list from user.
    :type my_list: list.
    :return: my_shift_list
    :rtype: list with str items"""
    my_list.append("")
    my_list[-1] = my_list[0]
    my_shift_list = my_list[1:-1] + [my_list[-1]]
    print(my_shift_list)


list = input('please type a group of numbers\\words devided by "," (without space):')
print("your list is: ")
print(list)
list = list.split(",")
print("your new updated list with the first item to the last is:")
shift_left(list)
