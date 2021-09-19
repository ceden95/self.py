#the program convert degrees from F to C and the opposite.

temp = input("Insert the temperature you would like to convert(with a 'C' or 'F' mark):")
temp_type = temp[-1].upper()
temp_number = float(temp[:-1])
C_to_F = str(((9*temp_number)+(160))/5)
F_to_C = str((5*temp_number-160)/9)
if (temp_type == "C"):
	print(C_to_F + "F")
elif (temp_type == "F"):
	print (F_to_C + "C")
else:
	print("told you to mark the temperature")



