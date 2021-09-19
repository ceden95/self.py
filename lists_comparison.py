#the program print True if the items in the 2 lists the user choosed are equal. else- prints False.

def main(): 
    l1 = input("type your first list of float and int numbers devided by the sign ',': ")
    list1 = l1.split(",")
    print("this is your list:")
    print(list1)
    l2 = input("now type your second list by the same guidelines: ")
    list2 = l2.split(",")
    print(list2)
    print("are they the same lists??")
    lists_check = are_lists_equal(list1, list2)
    print(lists_check)

def are_lists_equal(list1, list2):
    """the function return true is the items in the 2 lists are the same.
    sorted():this function orginizes the item of the list
    :return: True if its the same, False if they are different
    :rtype: string"""
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

main()
