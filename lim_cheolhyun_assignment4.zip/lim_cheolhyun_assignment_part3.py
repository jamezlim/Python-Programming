# Input number of columns and validate whether positive 
columns = int (input ("How many columns?"))
while columns < 1:
    print ("Invalid entry, try again!")
    columns = input ("How many columns?")

# Direction
direction = input(" Direction? (l)eft or (r)ight:")
while direction != "l" and direction != "r":
    print ("Invalid entry, try again!")
    direction = input(" Direction? (l)eft or (r)ight:")

# Right Side
if direction == "r":

    i = 0
    while i < columns:
        print (' '*i,"*")
        i += 1
        
    i = i - 2
    while i != -1:
        print (' '*i,"*")
        i -= 1
# Left side  
elif direction == "l":

    i = columns - 1
    while i != 0:
        print (' '*i,"*")
        i = i - 1

    i = 0
    while i < columns:
        print (' '*i,"*")
        i += 1
