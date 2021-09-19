#the program prints a new list with the odd items on it and the last item.
#the  original list made by the user. 

def main():
    a_list = input("create a sequence of words/numbers devided by the sign ','.\nmake sure the number of sequence is even:")
    a_list = a_list.split(",")
    list_length = int(len(a_list))
    while list_length % 2 == 1:
        a_list = input("are you sure its even? please type again! (make sure is evenn):")
        a_list = a_list.split(",")
        list_length = int(len(a_list))   
    format_list(a_list) 

    
def format_list(my_list):
    """the function creats a new list with the odd items on it(starting from the first). 
    the two last item gathers into one and separated by the word 'and'.
    :param my_list: list made by user
    :my_list type: list
    :return: list with the odd numbers + the last item.
    :rtype: list"""
    sliced_no_last_item = my_list[::2]
    last_item = "and " + str(my_list[-1])
    new_list = sliced_no_last_item + [last_item]
    print(new_list)



main()