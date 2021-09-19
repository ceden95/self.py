#the program prints 'ok' if the input from user is palindrome
#(still the same word backward)
#OR 'not' if its not palindrome

def isPalindrome(p):
"""function return true if 'p' is palindrome,
else, return false"""
    return p == p[::-1]
    
p = input("please enter a word:")
pali = isPalindrome(p)

if pali:
    print("OK")
else:
    print("NOT")