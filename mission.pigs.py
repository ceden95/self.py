#this program calculate the number of bricks each pig owns by input the user choose.

#the program receive a 3 digit number from user.
total_bricks = input("please enter three digits number:")
print("the number you chose is", total_bricks)
total_bricks = (int(total_bricks))

#every pig get 1 digit from the number the user choosed.(from left to right.
pig_A = (total_bricks)%10
total_bricks = int((total_bricks)/10)
pig_B = (total_bricks)%10
pig_C = (total_bricks)//10

#the program prints the total of bricks which is the addition of all 3 numbers.
total_bricks_collected = (pig_A)+(pig_B)+(pig_C)
print("1.the total number of bricks the pigs collected was", total_bricks_collected)

#the program prints the number of bricks each pig gets equally(no residue).
equal_bricks = (total_bricks_collected)//3
print("2.the number of bricks each pig gets equally is", equal_bricks)

#the program prints the remain bricks left from deviding bricks equally between the pigs.
residue = (total_bricks_collected)%3
print("3.if the number of bricks dont split equally between the 3 pigs, the residue is", residue)

#the program prints True if the devision of 3 is without remainder, else- False.
print("4.", residue == 0)
