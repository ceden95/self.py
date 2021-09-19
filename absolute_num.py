#the program prints True if the 3 numbers the user gives are in certain absolute distance with each other
#according to the function conditions, else- False.

def distance(num1, num2, num3):
"""function return true if num2\num3 in absolute distance with num1 AND
num2\num3 in absolute distance >=2 with the other 2 numbers"""
    if abs(num1-num2)==1 and (abs(num2-num3)>=2 and abs(num1-num3)>=2):
        return True
    elif abs(num1-num3)==1 and (abs(num2-num3)>=2 and abs(num1-num2)>=2):
        return True
    else :
        return False

num1 = int(input("type your first number:"))
num2 = int(input("now the second:"))
num3 = int(input("and now the third!!:"))

print(distance(num1, num2, num3))