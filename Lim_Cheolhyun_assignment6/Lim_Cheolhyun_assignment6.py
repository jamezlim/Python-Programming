import myfunctions
import random 

# Number of attempts
attempt = int(input("How many problems would you like to attempt?"))
while attempt <= 0:
    print("Invalid number, try again\n")
    attempt = int(input("How many problems would you like to attempt?"))

# Width of numbers 
width = int(input("How wide do you want your digits to be? 5-20:"))
while width < 5 or width >20:
    print ("Invalid width, try again\n")
    width = int(input("How wide do you want your digits to be? 5-20:"))

# Drill mode (Option 3)    
drill = input ("Would you like to activate 'drill' mode? yes or no:")

# Counter variable for correct answers 
correct_answers = 0

# 
for i in range (attempt):
    print ("What is...")

    # Validating for dividable numbers 
    x = random.randint(0,9)
    y = random.randint(0,9)
    z = random.randint(1,4)
    while (z == 4 and y == 0) or (z == 4 and (x/y).is_integer() == False):
        x = random.randint(0,9)
        y = random.randint(0,9)
        z = random.randint(1,4)    

    # Calling number function for x
    if x == 0:
        myfunctions.number_0(width)
    elif x == 1:
        myfunctions.number_1(width)
    elif x == 2:
        myfunctions.number_2(width)
    elif x == 3:
        myfunctions.number_3(width)
    elif x == 4:
        myfunctions.number_4(width)
    elif x == 5:
        myfunctions.number_5(width)
    elif x == 6:
        myfunctions.number_6(width)
    elif x == 7:
        myfunctions.number_7(width)
    elif x == 8:
        myfunctions.number_8(width)
    elif x == 9:
        myfunctions.number_9(width)

    # Calling calculation function for z 
    if z == 1:
        z = "+"
        myfunctions.plus(width)
    elif z == 2 :
        z = "-"
        myfunctions.minus(width)
    # Option 1
    elif z == 3 :
        z = "*"
        myfunctions.multiply(width)
    # Option 2
    elif z == 4:
        z = "/"
        myfunctions.division(width)

    # Calling number function for y
    if y == 0:
        myfunctions.number_0(width)
    elif y == 1:
        myfunctions.number_1(width)
    elif y == 2:
        myfunctions.number_2(width)
    elif y == 3:
        myfunctions.number_3(width)
    elif y == 4:
        myfunctions.number_4(width)
    elif y == 5:
        myfunctions.number_5(width)
    elif y == 6:
        myfunctions.number_6(width)
    elif y == 7:
        myfunctions.number_7(width)
    elif y == 8:
        myfunctions.number_8(width)
    elif y == 9:
        myfunctions.number_9(width)

    # Asking user for answer 
    print ("=",end ="")
    user_answer = int (input ())

    # Checking answer 
    answer = myfunctions.check_answer (x,y,user_answer,z)
    if drill == "yes":
        while answer == False:
            print ("Sorry, that's not correct.")
            # Ask again 
            print ("=",end ="")
            user_answer = int (input ())
            answer = myfunctions.check_answer (x,y,user_answer,z)
        print ("Correct!")
        print ()
        continue
    if answer == True:
        correct_answers +=1
        print ("Correct!")
    elif answer == False:
        print ("Sorry, that's not correct.")
    print ()

# Drill mode print out "Thanks for playing!"
if drill == "yes":
    print ("Thanks for playing!")
    
# After all attempts printing out number of problems correct     
else :
    print ("You got",correct_answers,"out of",attempt,"correct!")
    
        


