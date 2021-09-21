#the program sort a list of tuples. each tuple has 2 items.(product, price).
#the list sorted by prices from the most expensive product to the cheapest.
#the user choose the quantity of products, the products and the prices.

def main():
    listFromUser = getListOfTuple()
    sort_prices(listFromUser) 
    
def getListOfTuple():
    """the function return a list made from number of tuples the user choose.
    the tuples made in getTupleFromUser() function.
    :return: list of tuple items.
    :rtype: list"""
    num_of_tuples = input("write the number of items you want to sort: ")
    list_of_tuples = []
    for i in range(int(num_of_tuples)):
        print("Enter details for item number %d :" % int(i+1))
        tupleFromUser = getTupleFromUser()
        list_of_tuples.append(tupleFromUser)
    return list_of_tuples

def getTupleFromUser():
    """the function creates a tuple of two items.
    :return: (product, price of product)
    :rtype: tuple"""
    item = input("type an item you can find in the market: ")
    price = float(input("what's its price? "))
    return item,price

def sort_prices(listFromUser):
    """the function sort the list of tuple by the product prices.
    :param listFromUser: list of tuple items. each item:(product, price)
    :listFromUser type: list
    :return: sorted list of the tuples, from the most expensive product to the cheapest.
    :rtype: list."""
    sortedfromlow = sorted(listFromUser, key=keyforsort, reverse=True) 
    print(sortedfromlow)

def keyforsort(item):
    """the function return the 2nd item from the tuple made in getTupleFromUser().
    :param item: (product, price)
    :item type: tuple
    :return: price
    :rtype: int"""
    return item[1]

main()