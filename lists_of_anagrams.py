#the program gets a list of several words from user by his choise(each word is a srtring)
#the program return a list of lists, each list in the list contains a group of words contains with the exact same letters.


def main():
    str_num = int(input("times of strings you'd like to have in the list: "))
    list_of_strings = listOfStrings(str_num)
    print(list_of_strings)
    end_list = sort_anagrams(list_of_strings)

    print(end_list)

def listOfStrings(str_num):
    """the function creats a list of words the user chooses, in the length of the number from str_mun.
    :param str_num: a number the user choosed.
    :str_num type: int.
    :return: a list of strings in the length of the number the user choosed
    :rtype: list"""
    listOfStrings = []
    for i in range(0, str_num):
        stringForList = input("type in your word: ")
        listOfStrings.append(stringForList)
    return listOfStrings

def sort_anagrams(list_of_strings):
    """the function gathering the word contian with the same letters to individual list.
    :param list_of_strings: list of str
    :list_of_strings type: str
    :return: list of lists' each list contains string\strings.
    :rtype: list"""
    bigList = []
    for string in list_of_strings:
        listToList = [] 
        for string2 in list_of_strings:
            if sorted(string) == sorted(string2):
                listToList.append(string2)
    
        bigList.append(listToList)
 
    newList = []
    #Delete duplicates from bigList:
    prevItem = ""
    for list1 in bigList:
        if prevItem != list1:
            newList.append(list1) 
        prevItem = list1
        
    return newList



main()