#the program creates a new list(from the list the user created) of numbers bigger then the number the user choosed.

def main():
    list1 = input('type a sequence of random numbers devided by the sign ",": ')
    my_list = list1.split(",")
    n = int(input("type a number which represent the smallest number in your new list: "))
    is_greater(my_list, n)


def is_greater(my_list, n):
    """the fuction creates a list of numbers from my_list
    from numbers bigger them number n.
    :param my_list: list of numbers
    :my_list type: list
    :param n: number from user
    :n type: int"""
    my_new_list = []
    for num in my_list:
        num = int(num)
        if num > n:
            my_new_list.append(num)
        else: 
            continue
    print(my_new_list)
    
main()