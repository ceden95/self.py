#the program uses data from file and return it according to the option the user chooses.
#'sort' returns a sorted list without duplacations.
#'rev' returns reversed sentence.
#'last' returns the number of lines of the text from the input the user choosed.


def main():   
    file1 = r"C:\python course\9.1.2\textFor9.1.2.txt" 
    inputFromUser = input("please choose one of the following options: sort, rev or last: ")
    file1ToUserInput(file1, inputFromUser)

def file1ToUserInput(file1, inputFromUser):
    """the func return a customized information according to the user's choice.
    :param file1: file path to a text
    :file1 type: str
    :param inputFromUser: input from user- given 3 optiond, needs to choose one.
    :inputFromUser type: string.
    :return: according to inputFromUser 's choise.
    'sort' returns a sorted list without duplacations.
    'rev' returns reversed sentence.
    'last' returns the number of lines of the text from the input the user choosed."""
    
    emptyList = []
    fileToRead = open(file1, "r")
    readedFile = fileToRead.read()

    if inputFromUser == "sort":
        readedFile = readedFile.replace("\n"," ")
        fileList = readedFile.split(" ") 
        fileList.sort()
        for word in fileList:
            if word not in emptyList:
                emptyList.append(word)
    print(emptyList)
    
    if inputFromUser == "rev":
        lines = readedFile.split("\n")
        for line in lines: 
            print(line[::-1])

    if inputFromUser == "last":
        inputForLast = input("enter a number: ")
        lines = readedFile.split("\n")
        for i in range(0,int(inputForLast)): 
            print(lines[i])

main()
