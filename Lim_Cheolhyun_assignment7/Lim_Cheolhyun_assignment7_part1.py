#Part 1a
valid1 = True                        
while valid1:
    name = input ("Please enter a username:")
    if len(name) < 8 or len(name) > 15:
        print ("Username must be between 8 and 15 characters.\n")  
        continue 
    elif name.isalnum()== False:
        print("Username must contain only alphanumeric characters.\n")
        continue
    elif name[0].isdigit() :
        print ("The first character in your username cannot be a digit.\n")
        continue 
    elif name.islower():
        print ("Your username must contain at least one uppercase character.\n")
        continue
    elif name.isupper():
        print ("Your username must contain at least one lowercase character.\n")
        continue
    elif name.isalpha():  # == True not necessary 
        print ("Your username must contain at least one digit.\n")
        continue
    
    valid1 = False 
print ("Your username is valid!\n")

#Part 1b

valid2 = True
while valid2:
    password = input ("Please enter a password:")
    if len(password) < 8: 
        print("Passwords must be at least 8 characters long.\n")
        continue 
    elif name in password :
        print ("You cannot use your username as part of your password.\n")
        continue
    elif password.islower():
        print ("Your password must contain at least one uppercase character.\n")
        continue
    elif password.isupper():
        print ("Your password must contain at least one lowercase character.\n")
        continue
    elif password.isalpha():
        print ("Your password must contain at least one digit.\n")
        continue
    # varify whether the password contains special characters at all

    flag = ""
    for c in password:
        if c.isdigit() or c.isupper() or c.islower():
            continue
        else:
            flag = 1 #has special characters 
            break
        
    if flag != 1:
        print ("Your password must contain at least one 'special' character.\n")
        continue
    # password has special character in it by this point
    invalid = ""
    for c in password:
        if c.isdigit() or c.isupper() or c.islower():
            continue
        elif ord(c)<39 and ord(c)>34:
            continue
        else : # has something other than designated characters 
            invalid = 1
            break
    if invalid == 1:
        print ("Your password contains at least one invalid character.\n")
        continue
    valid2 = False 
print ("Your password is valid!")
   
        

            
