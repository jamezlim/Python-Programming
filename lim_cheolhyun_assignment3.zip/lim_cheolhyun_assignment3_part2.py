# Checking whether the date is valid
date = False 
while date == False:
    month = int (input ("Enter a month (1-12):"))
    day = int (input ("Enter a day (1-31):"))
       
    if month > 12 or month < 1:
        print ("Sorry, that's not a valid date.")
    elif day > 31 or day < 1:
        print ("Sorry, that's not a valid date.")
    elif month == 2 :
        if day > 28 :
            print ("Sorry, that's not a valid date.")
        else :
            date = True
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day >30:
            print ("Sorry, that's not a valid date.")
        else :
            date = True
    else:
        date = True
# Changing numeric months into calendar months

monthstring = ""

if month == 1:
    monthstring = "January"
elif month == 2:
    monthstring = "Feburary"
elif month == 3:
    monthstring = "March"
elif month == 4:
    monthstring = "April"
elif month == 5:
    monthstring = "May"
elif month == 6:
    monthstring = "June"
elif month == 7:
    monthstring = "July"
elif month == 8:
    monthstring = "August"
elif month == 9:
    monthstring = "September"
elif month == 10:
    monthstring = "October"
elif month == 11:
    monthstring = "November"
elif month == 12:
    monthstring = "December"
# now month and monthstring is linked 

# Checking wheter date is during the Spring 2015 term
                   
if month == 1:
    if day < 26:
        print (monthstring, day, "is before the start of Spring 2015 term.")
elif month == 5:
    if day > 12:
        print (monthstring, day, "is after the Spring 2015 term.")
elif month > 5 :
    print (monthstring, day, "is after the Spring 2015 term.")

# Filtering out holidays
elif month == 2 and day == 16:
    print (monthstring, day, "is Presidents Day. NYU is not open on this day.")
elif month ==3:
    if day==16 or day==17 or day==18 or day==19 or day==20 or day==21 or day==22:
           print (monthstring, day, "is during Spring Break. NYU is not open on this day.")

# All other days are normal school days 
else :
    print (monthstring, day, "is not a holiday at NYU. NYU is open on this day.")

#
    
      

    
