valid_number = True 
while valid_number :
    user_number = input ("Enter a start and end number, separated by a comma:")
    user_number = user_number.strip()
    user_number = user_number.split(',')
    # ['5','23']
    x = int(user_number[0])
    y = int(user_number[1])
    if x <= 0 or y <= 0:
        print ("Sorry, the start and end must be positive")
        continue
    elif x >= y:
        print ("End number must be greater than start number")
        continue

    valid_number = False
#Now you have a vadid input for x and y
# ex) 5 23


# Validating Prime Number (keep in mind of perfect square numbers) 
def is_prime(x):
    prime=True 
    if x == 2:
        return prime 
    elif x > 2: 
        for i in range(2,x): 
           if x%i==0: 
               prime = False 
        return prime

# Printing All prime numbers in range 
print()
for i in range(x,y+1):
    prime = is_prime(i)
    if  prime == True:
        print (i)
    




            

        

    
