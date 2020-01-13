beer = input ("How many bottles of beer on the wall?")

while not beer.isnumeric() or  int(beer) < 1 or int (beer) > 99 :
    print ("Sorry, that's not a valid number of bottles. Try again.","\n")
   
    beer = input ("How many bottles of beer on the wall?")
        
print ()
print ("OK, here we go!")

# Change the variable into an int before starting for loop 
beer = int (beer)
for i in range ( beer,0,-1):
            if i == 2:
                print ("2 bottles of beer on the wall, 2 bottles of beer.")
                print ("Take one down, pass it around, 1 bottle of beer on the wall.") 
                continue
            elif i == 1:
                print ("1 bottle of beer on the wall, 1 bottle of beer.")
                print ("Take it down, pass it around, no more bottles of beer on the wall!")
                continue 
            print (i,"bottles of beer on the wall,", i,"bottles of beer.")
            i -= 1
            print ("Take one down, pass it around,", i,"bottles of beer.")
             
