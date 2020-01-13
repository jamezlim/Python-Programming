# Validating whether amount of sticks is between 100 and 10 
sticks = int( input ("How many sticks are on the table? (enter a number between 10 and 100):"))

while sticks < 10 or sticks > 100 :  
    print ("Invalid # of sticks, please try again.")
    sticks = int( input ("How many sticks are on the table? (enter a number between 10 and 100):"))

# while true keep going
while sticks > 0:

    #Player 1
    print ()
    print ("There are",sticks,"sticks on the table")
    print ("Turn: Player 1")

    # Validating number of sticks removed are 1,2 or 3
    removed_sticks1 = int (input ("How many sticks do you want to remove from the table? (1, 2 or 3):"))
    while removed_sticks1 < 0 or removed_sticks1 > 3:
        print ("Invalid number of sticks, try again.")
        print ()
        print ("There are",sticks,"sticks on the table")
        print ("Turn: Player 1")
        removed_sticks1 = int (input ("How many sticks do you want to remove from the table? (1, 2 or 3):"))

    # Validating number of sticks removed compared to number of sticks left
    while removed_sticks1 > sticks:
        print ("You can't take that many sticks off of the table. Try again.")
        print ()
        print ("There are",sticks,"sticks on the table")
        print ("Turn: Player 1")
        removed_sticks1 = int (input ("How many sticks do you want to remove from the table? (1, 2 or 3):"))

    # After valid number input, substitute the sticks variable
    sticks = sticks - removed_sticks1
    if sticks < 1 :
        print ("Player 1 loses!")
        break

    #Player 2
    print ()
    print ("There are",sticks,"on the table")
    print ("Turn: Player 2")

    # Validating number of sticks removed are 1,2 or 3 
    removed_sticks2 = int (input ("How many sticks do you want to remove from the table? (1, 2 or 3):"))
    while removed_sticks2 < 0 or removed_sticks2 > 3:
        print ("Invalid number of sticks, try again.")
        print ()
        print ("There are",sticks,"on the table")
        print ("Turn: Player 2")
        removed_sticks2 = int (input ("How many sticks do you want to remove from the table? (1, 2 or 3):"))

    # Validating number of sticks removed compared to number of sticks left
    while removed_sticks2 > sticks:
        print ("You can't take that many sticks off of the table. Try again.")
        print ()
        print ("There are",sticks,"on the table")
        print ("Turn: Player 2")
        removed_sticks2 = int (input ("How many sticks do you want to remove from the table? (1, 2 or 3):"))
        
    # After valid number input, substitute  
    sticks -= removed_sticks2
    if sticks < 1:
        print ("Player 2 loses!")    
   
