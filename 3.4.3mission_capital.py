#the program gets a random word from user and prints back the word 
#with capital letters at the second half of the word.
#if number of letters is odd the second half 1 letter bigger.

word = input("please wright a random word that pops in your mind:")
total = len(word)
number_of_caps = int(total/2)
caps = word[number_of_caps: ]
second_part = caps.upper()
not_capital = (total)-(number_of_caps)
first_part = word[:(number_of_caps)]
print(first_part + second_part)
