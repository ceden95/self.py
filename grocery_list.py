#the program gets a grocery list from user.
#the program has menu from 1-9; each number return a diferrent output.

def main(): 
    grocery_list = input('type your grocery list devided by "," sign: ')
    grocery_list = grocery_list.split(",")
    pick_a_num = int(input("pick a number from 1-9: "))
    while pick_a_num != 9:
        grocery_list = menu(pick_a_num,grocery_list)
        pick_a_num = int(input("pick a number from 1-9 "))
    print("Thank you!!!!")  



def menu(pick_a_num, grocery_list):
    """the function a diferrent __according to the number the user choosed.
    :param pick_a_num: number from 1-9 from user.
    :pick_a_num type: int
    :param grocery_list: list of grocery products.
    :grocery_list type: list"""
    if pick_a_num == 1:
        print_list(grocery_list)
    elif pick_a_num == 2:
        length_list(grocery_list)
    elif pick_a_num == 3:
        is_product_in_list(grocery_list)
    elif pick_a_num == 4:
        product_quantity(grocery_list)
    elif pick_a_num == 5:
        grocery_list = remove_product(grocery_list)
    elif pick_a_num == 6:
        grocery_list = add_product(grocery_list)
    elif pick_a_num == 7:
        invalid_product(grocery_list)
    elif pick_a_num == 8:
        grocery_list = duplication_removal(grocery_list)
    return grocery_list



def print_list(grocery_list):
    """print the user's grocery list"""
    print(grocery_list)

def length_list(grocery_list):
    """print the number of item im the grocery list"""
    length = len(grocery_list)
    print("you have " + str(length) + " items on your grocery list")

def is_product_in_list(grocery_list):
    """function ask from user to type a product.
    the function answer if the product the user typed is in the grocery list or not."""
    print("check if you have a product in your list.")
    product = input("pick a product: ")
    if product in grocery_list:
        print(product + " is on your list")
    elif product not in grocery_list:
        print(product + " is NOT on your list")

def product_quantity(grocery_list):
    """function ask from user to type a product.
    the function answer how many times the product is in the grocery list."""
    product = input("type in a product to see how mamy times its in your list: ")
    product_quantity = str(grocery_list.count(product))
    print(product + " is " + product_quantity + " times on your list")

def remove_product(grocery_list):
    """the function removes a product from grocery list according to user's choice"""
    remove_product = input(" pick an item you'd like to remove from your list: ")
    grocery_list.remove(remove_product)
    print(remove_product + " removed, your new list is: ")
    print(grocery_list)
    return grocery_list

def add_product(grocery_list):
    """the function adds a product to grocery list according to user's choice"""
    add_product = input("add a product to your list: ")
    grocery_list.append(add_product)
    print("your new grocery list is:")
    print(grocery_list)
    return grocery_list

def invalid_product(grocery_list):
    """the function prints 'invalid products': products shorter then 3 letters\
    products with numbers in the word."""
    invalid_products = []
    for item in grocery_list:
        if item.isalpha() == False or len(item) < 3:
            invalid_products.append(item)
    print("these are the invalid products on your list")
    print(invalid_products)

def duplication_removal(grocery_list):
    """function removes duplications of products from grocery list."""
    sorted_list = sorted(grocery_list)
    new_list = []
    prev_item = ""
    for item in sorted_list:
        if item != prev_item:
            new_list.append(item)
            prev_item = item
    print("this is your list without duplications")
    print(new_list)
    return new_list

main()

