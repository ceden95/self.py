#the program recieves a file of string.
#the string is made from consecutive numbers devided by ',' sign(not by order), and one missing number.
#the function 'who_is_missing' creates another txt file of a string with the missing number from the first file.

def main():
    file_name = "C:\python course\9.2.3\9.2.3.fileOfNumbersAndOneMissing.txt"
    who_is_missing(file_name)


def who_is_missing(file_name):
    """the function creates another txt file from
    the missing number in the file_name.
    :param file_name: file path to string of consecutive numbers and 1 missing.
    :file_name type: str.
    :return: """
    
    openedFile = open(file_name, "r") 
    readed_file = openedFile.read()
    print("this is the file: " + readed_file)
    openedFile.close()
    stringOfNum = readed_file.replace("\n", "")
    listOfStrNum = stringOfNum.split(",")
    listOfInts = [] 
    for number in listOfStrNum:
        a = int(number)
        listOfInts.append(a)
    print("this is the list of numbers from file: ")
    print(listOfInts)
    listOfInts.sort()
    print("this is the sorted list")
    print(listOfInts)

    duplicatrlist = listOfInts
    lenoflist = len(listOfInts)
    for i in range(0, lenoflist):
        if listOfInts[i] + 1 == duplicatrlist[i + 1]:
            continue
        else:
            missing_number = listOfInts[i] + 1
            missing_number_str = str(missing_number)
            print("the missimg number on the sequence is number: ")
            print(missing_number)
            break 
       
    missing_number_str = str(missing_number) 
    
    file_for_missing_number = "C:\python course\9.2.3\empty.txt"
    opened_file_for_missing_number = open(file_for_missing_number, "w")
    opened_file_for_missing_number.write(missing_number_str)
    opened_file_for_missing_number.close()
    return missing_number 

main()