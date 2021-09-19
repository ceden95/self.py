#the program prints back the day of the date the user choosed.

date = input(" please write a date which contains dd/mm/yyyy:")
dd = int(date[:2])
mm = int(date[3:5])
yyyy = int(date[-4:])

import calendar
what_day = calendar.weekday(yyyy, mm, dd)

if what_day == 0:
    print("monday")
elif what_day == 1:
    print("tuesday")
elif what_day == 2:
    print("wednesday")
elif what_day == 3:
    print("Thursday")
elif what_day == 4:
    print("Friday")
elif what_day == 5:
    print("Saturday")
elif what_day == 6:
    print("Sunday")
