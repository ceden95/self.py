#the program creates a new list without repetition of letters.
#list made by user.

def main():
    my_str = input("type a word like 14 years old teenager(llikeeeee thhhatttt yooo): ")
    sequence_del(my_str)
    
def sequence_del(my_str):
    """creates a new string withoout repetition"""
    prev_letter = ""
    new_str = ""
    for letter in my_str:
        if letter != prev_letter:
            new_str += letter
            prev_letter = letter
    print(new_str)
        
main()
