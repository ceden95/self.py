#the program prints the sum of all 3 numbers of age from user.
#in case the number is in the tuple age_to_zero(in fix_age func), then the number is calculated as 0.

def fix_age(age):
"""the function return 0 if the age is in age_to_zero,
else, return the same number"""
    age_to_zero = (13, 14, 17, 18, 19)
    if age in age_to_zero:
        return 0
    else:
        return age


def filter_teens(a=13 ,b=13 ,c=13):
"""the function adding all 3 numbers together
default is 13."""
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    total_age = int(a) + int(b) + int(c)
    return total_age

age1 = int(input("type first age:"))
age2 = int(input("type second:"))
age3 = int(input("type third:"))

print(filter_teens(age1, age2, age3))