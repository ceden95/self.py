#the function creates a list of numbers from 0 to end_number.
#if number % 7 = 0/end with digit 7/end_number then replace it with 'BOOM'

def main():
    end_number = int(input("type a number: "))
    seven_boom(end_number)

def seven_boom(end_number):
    """the function creates a list of numbers from 0 to end_number
    if number % 7 = 0/end with digit 7/end_number then replace it with 'BOOM'"""
    list_a = []
    for number in range(0,end_number + 1,1):
        if number == 0:
            list_a.append("BOOM") 
        elif number % 7 == 0:
            list_a.append("BOOM")
        elif '7' in list(str(number)):
            list_a.append("BOOM")    
        else:
            list_a.append(number)
    print(list_a)
    
    main()