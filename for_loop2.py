#the program creates a list of two numbers- the first is the number of numbers, the second is the number of letters.)


def main():
    my_str = input("type a sentence with mumbers and letters: ")
    count_list = numbers_letters_count(my_str)
    print(count_list)

def numbers_letters_count(my_str):
    """the function return list of number of numbers and number of letters
    fron my_str
    :param my_str: str of letters and numbers
    :my_str type: str
    :return: list of 2 numbers
    :rtype: list"""
    numberCounter = 0
    for letter in my_str:
        if letter.isnumeric() == True: 
            numberCounter += 1       
        else:
            continue   
    strlen = len(my_str)
    letterlen = strlen - numberCounter
    return ([numberCounter] + [letterlen])
main()
    