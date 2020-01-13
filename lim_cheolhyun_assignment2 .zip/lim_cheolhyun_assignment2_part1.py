#Part 1 dynamic tip calculator 

print("Hello! I'm here to help you calculate your tip.")

#Basic Info
total_dollars = float(input("How much was your bill? (enter as a number without dollar signs or commas):"))
tip_percentage = int(input("What percentage tip would you like to leave? (enter just a number):"))

print("Thanks!")

#Tip 
total_tip = total_dollars * tip_percentage * 0.01
total_tip_2 = float (format (total_tip, ".2f"))
print("You need to leave $",total_tip_2,"as a tip.")

#Final Bill 
total_bill = total_dollars + total_tip_2
total_bill_2= float (format (total_bill, ".2f"))
print("Your total bill will be $",total_bill_2,)

#First you start off with your bill and the tip percentage. Changing the input value into floats and integers needed
#The total tip should be formatted to two decimals then made into a float.
#Finally you add up the total tip and your total bill to get the final bill 
                      
