#the program gest two tuples.
#the program return a tuple contains all the possible pairs can be creates from 
#the tuples. the pairs are tuples as well.


def main():
    inputFromUser = input('type numbers devided by the sign ",": ') 
    first_tuple = strListToTuple(inputFromUser)
    print(first_tuple) 
    inputFromUser2 = input('type list of numbers again in the same way(","): ') 
    second_tuple = strListToTuple(inputFromUser2)
    print(second_tuple)
    mult_tuple(first_tuple, second_tuple)


def strListToTuple(inputFromUser):
    """the function return a tuple of int numbers.
    :param inputFromUser: input from user fo numbers devided by ',' sign.
    :inputFromUser type: string.
    :return: tuple of int numbers
    :rtype: tuple"""
    listOfStr = inputFromUser.split(",")
    emptyList = []
    for num in listOfStr:
        intInList = int(num) 
        emptyList.append(intInList)
    emptyList = tuple(emptyList)
    return emptyList


def mult_tuple(first_tuple, second_tuple):
    """returns all the possible sequences for the two tuplse provided.
    :param first_tuple, second_tuple: tuples of ints.
    :return: all the possible sequences for the two tuplse provided
    :rtype: tuple."""
    emptyList = []
    for number in first_tuple:
        for secNum in second_tuple:
            tupleintuple = (number, secNum)
            emptyList.append(tupleintuple)
    for number in second_tuple:
        for secNum in first_tuple:
            tupleintuple = (number, secNum)
            emptyList.append(tupleintuple)
    newTuple = tuple(emptyList)
    print(newTuple)
    

main() 