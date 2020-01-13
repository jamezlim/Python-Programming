import random

# Asking user for an input
sides = int (input ("How many sides are on your dice?"))

# Validating whether number is int 
while sides < 3:
    print ("Sorry, that's not a valid size value. Please choose another positive number.")
    sides = int (input ("How many sides are on your dice?"))
print ()
print ("Thanks! Here we go...")
print ()

# Rolling two dice
die_1 = 0
die_2 = 0

# Defining variables 
trial = 0
double = -1
die_1_total = 0
die_2_total = 0

#as long as die-1 is not 1 or die_2 is not 1 keep going
while die_1 != 1 or die_2 != 1:
    trial += 1
    die_1 = random.randint (1, sides)
    die_2 = random.randint (1, sides)
    
    print (trial, end = ".")
    print (" die number 1 is",die_1,"and die number 2 is",die_2)
    # adding each roll to the die_total variable
    die_1_total += die_1
    die_2_total += die_2

    # making the double variable a counting variable 
    if die_1 == die_2:
        double += 1
print ()           
print ("You got snake eyes! Finally! on try number",trial,end = "")
print ("!")
print ("Along the way you rolled doubles", double,"times")

# Calculating the average roll
die_1_avg = die_1_total / trial
die_2_avg = die_2_total / trial

# Formatting to two decimal places 
formated_die_1_avg = format (die_1_avg, ".2f")
formated_die_2_avg = format (die_2_avg, ".2f")

print ("The average roll for die #1 was", formated_die_1_avg)
print ("The average roll for die #2 was", formated_die_2_avg)
