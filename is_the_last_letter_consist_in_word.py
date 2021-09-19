#the program prints "True" when the last letter apearse in the specific word, not including the last letter
#otherwise- prints "False"

def last_early(my_str):
    last_letter = my_str[-1]
    if last_letter in my_str[0:-1]:
        return True
    else:
        return False
        
word = input("please enter a word:")
a = last_early(word) 
print(a)


