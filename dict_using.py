#the program runs a menu to several actions according to the info in thw dictionary given.

def main():
    new_dict = {"first_name" : "Mariah", "last_name" : "Carey", "birth_date" : "27.03.1970", "hobbies" : ("Sing", "Compose", "Act")}
    print(new_dict)
    picked_num = int(input("type a number between 1-7: "))
    pickedFromDict(picked_num, new_dict)


def pickedFromDict(picked_num, new_dict):
    """the function print a data from dict 'new_dict' according to the number(picked_n)
    the user choosed.
    :param picked_num: number betweem 1-7 the user choosed.
    :picked_num type: int
    :paran new_dict: dictionary with info of mariah carey.
    :new_dict type: dict"""
    #1-printing mariah's last name
    #2-printing mariah's birth date
    #3-printing mariah's hobbies
    #4-printing mariah's last hobbie
    #5-adds "coocking" to mariah's hobbies and printing mariah's updated hobbies
    #6-printing mariah's birth date into tuple of 3 numbers
    #7-printing the dict with a new key- 'age'
    if picked_num == 1:
        print(new_dict["last_name"])
    elif picked_num == 2:
        print(new_dict["birth_date"])
    elif picked_num == 3:
        print(len(new_dict["hobbies"]))
    elif picked_num == 4:
        print((new_dict["hobbies"][-1]))  
    elif picked_num == 5:
        new_dict["hobbies"] = ("Sing", "Compose", "Act", "coocking")
        print(new_dict["hobbies"])
    elif picked_num == 6:
        a = new_dict["birth_date"].split(".")
        print(tuple(a))
    elif picked_num == 7:
        new_dict["age"] = "51"
        print(new_dict)

main()