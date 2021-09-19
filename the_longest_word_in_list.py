#the program  prints the longest word in the list the user makes.

def main():
    a = input("creat a sequence of random words devived by the sign ',' without spaces: ")
    list1 = a.split(",")
    print("this is your list")
    print(list1)
    print("the longest word in your list is:")
    longest_word = longest(list1)
    print(longest_word)

def longest(my_list):
    """the function return the longest word in the list
    :.sort(): defindes the list from the shortest to the longest word
    :param my_list: list from user of random words
    :my_list type: list.
    :return: the longest word(last)
    :rtype: str"""
    my_list.sort()
    last = my_list[-1]
    return last

main()
