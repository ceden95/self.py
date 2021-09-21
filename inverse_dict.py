#the program creates a new reverse mapping dictionary.(key to value and value to key(old dict to new dict))
#in case the old value is the same in more then 1 old key- new value is list of more then 1 old key.
#example: {key1 : value, key2 : value} ---> {value : [key1, key2]}

def main():
    my_dict = {"sunday" : 1, "monday" : 2, "tuesday" : 1 ,"wednsday" : 3, "thursday" : 2, "friday" : 3, "saturday" : 4}
    inverted_dict = inverse_dict(my_dict)
    print(inverted_dict)


def inverse_dict(my_dict):
    new_dict = {}
    for key in my_dict:
        value = my_dict[key]
        if value in new_dict.keys():
            new_list = new_dict[value]
            new_list.append(key) 
            new_dict[value] = sorted(new_list) 
        else:
            new_dict[value] = [key]
    return new_dict 

main()