#program gets an input of a sentance.
#the program prints a new sentance: 
#the letters that are identical to the first letter of the sentance 
#replacing with the letter "e".
#the first letter remains the same.
sen = input("hi please write a sentence:")
new_sen = sen[0]+sen[1:].replace(sen[0], "e")
print(new_sen)

