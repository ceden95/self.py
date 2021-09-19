#the program creates a list of squared numbers to the range of numbers the user choose.


def main():
    start = int(input("first number:"))
    stop = int(input(("second number(>= first number):")))
    squared_list = squared_numbers(start, stop)
    print(squared_list)


def squared_numbers(start, stop):
    """the function creates a list of squared numbers from the range given by the user
    :param start, stop: numbers choosed my user
    :start, stop type: int
    :return: list of squared numbers
    :rtype: list"""
    a = []
    while (start <= stop):
        a.append(start * start)
        start += 1
    return a


main()