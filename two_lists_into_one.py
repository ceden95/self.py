#the program creates one list from two lists(from user)
#not using '+' operator / extend method.

def main():
    x = input("write your first list by deviding each item with ',' sign:")
    list_x = x.split(",") 
    y = input("now write your second list by deviding each item the same way:")
    list_y = y.split(",")
    new_extended_list = extend_list_x(list_x, list_y)
    print(new_extended_list)

# not allowed to use '+' / extend method
def extend_list_x(list_x, list_y):
    """the function takes 2 lists a combining 
    them into one(list_y first, then list_x)
    :param list_x, list_y: lists created by user.
    :list_x, list_y type: list.
    :return: new extended list
    :rtype: list."""
    list_y[:0] = list_x
    return list_y


main()