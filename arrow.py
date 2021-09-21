#the program creates an arrow from sign the user choose.
#user also choose what is the longest line on the arrow.


def main():
    my_char = input("which sign you want the arrow would be made of? ")
    max_length = int(input("type a number which represent the longest line in the arrow: "))
    arrow(my_char, max_length)

def arrow(my_char, max_length):
    string_to_print = my_char
    for number in range(1,max_length):
        print (string_to_print)
        string_to_print += my_char
    for number in range(1,max_length + 1): 
        print (string_to_print)
        string_to_print = string_to_print[:-1]   
        
main()
    