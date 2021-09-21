#the program prints a dict of letters as a keys and number
#of times the letter is in the sentance as a value. sentance given by user.

def main():
    my_str = input("type a sentance: ")
    countDict = count_chars(my_str)
    print(countDict)

def count_chars(my_str):
    """the functoin returns a dict of letters as a keys and number
    of times the letter is in the sentance as a value
    :param my_str: sentance from input
    :my_str type: string
    :return: dictionary of leters as keys and numbers as value.
    :rtype: dict"""
    new_dict = {}
    for letter in my_str: 
        if letter.isalnum() == False:
            continue
        elif letter in new_dict.keys(): 
            continue
        else:
            count = my_str.count(letter)
            new_dict[letter] = count
        

    return new_dict

main()