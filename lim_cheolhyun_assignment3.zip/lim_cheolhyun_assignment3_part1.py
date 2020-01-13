print ("Valid Triangle Tester")

# Enter Three Points
x1 = float (input ("Enter the x value of the first coordinate"))
y1 = float (input ("Enter the y value of the first coordinate"))            
x2 = float (input ("Enter the x value of the second coordinate"))
y2 = float (input ("Enter the y value of the second coordinate"))
x3 = float (input ("Enter the x value of the Third coordinate"))
y3 = float (input ("Enter the y value of the Third coordinate"))

# Calculate Three Sides and Format 
side1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
side2 = ((x2-x3)**2 + (y2-y3)**2)**0.5
side3 = ((x3-x1)**2 + (y3-y1)**2)**0.5

side_1 = float( format (side1, ".2f"))
side_2 = float( format (side2, ".2f"))
side_3 = float( format (side3, ".2f"))

# Print out Sides
print ()
print ("The legth of each side of your test shape is:")
print ("Side 1:", side_1)
print ("Side 2:", side_2)
print ("Side 3:", side_3)

# Varify
print ()
if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1 :
    print ("This is a valid triangle!")
else:
    print ("This is not a valid triangle")

# First, ask the user for 3 x and y coordinates using the input operator and convert them into a float
# Then using the formula compute the length of three sides and format them to two decimal places as well as converting them to a float
# Print out each side and show them to the user
# Finally we use the if operator to verify whether the three sides satisfy the three condition and if it does we print out saying the triangle is valid
# Otherwise use the else operator for any triangle that do not satisfy any of these three conditions and print out "Not a valid triangle".




