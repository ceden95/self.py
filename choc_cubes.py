#the program gets 3 numbers from user: 
#number of small chocolate cubes(1 CM each), number of big chocolate cubes(5 CM each), and random number.
#the program prints True if the cubes can create a length equal to X, all cubes or only part of them
#if impossible- prints False.

def chocolate_maker(small, big, x):
"""the function return true if the small and big cubes can create a legth equal to X."""
    x = int(x)
    small_cm = int(small)
    big_cm = int(big) * 5
    miss_num = int(x)//5
    if (x%5 == 0) and (x <= big_cm):
        return True
    elif x <= small_cm:
        return True
    elif x > big_cm and x % big_cm <= small_cm:
        return True
    elif x < big_cm and x-(miss_num*5) <= small_cm:
                        
        return True
    else:
        return False

small_chocs = input("how many small chocolate cubes you have?")
big_chocs = input("and how many big ones??")
x = input("Enter a random number: ")
print(chocolate_maker(small_chocs, big_chocs, x))