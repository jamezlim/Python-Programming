#Part 1
#Function for Lines 

def horizontal_line(width):
     print ("*"*width)
     
def vertical_line(shift,height):
    for i in range (height):
        print (" "*shift+"*")

def two_vertical_lines(height,width):
    width = width - 2
    for i in range (height):
        print ("*"+" "*width+"*")


#Part 2
#Function for Numbers
        
#number_0
def number_0 (width):
    horizontal_line(width)
    two_vertical_lines(3,width)
    horizontal_line(width)

#number_1 
def number_1(width):
    vertical_line (width-1,5)

#number_2
def number_2(width):
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)
    vertical_line(0,1)
    horizontal_line(width)

#number_3
def number_3(width):
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)

#number_4
def number_4(width):
    two_vertical_lines(2,width)
    horizontal_line(width)
    vertical_line(width-1,2)

#number_5
def number_5(width):
    horizontal_line(width)
    vertical_line(0,1)
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)

#number_6
def number_6(width):
    horizontal_line(width)
    vertical_line(0,1)
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)

#number_7
def number_7(width):
    horizontal_line(width)
    vertical_line(width-1,4)

#number_8
def number_8(width):
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)

#number_9
def number_9(width):
    horizontal_line(width)
    two_vertical_lines(1,width)
    horizontal_line(width)
    vertical_line(width-1,2)

#Part 3
#Function for Addition/Subtraction

#addition
def plus(width):
    vertical_line(width//2,2)
    horizontal_line(width)
    vertical_line(width//2,2)

#subtraction
def minus(width):
    print()
    print()
    horizontal_line(width)
    print()
    print()

#multiplication
def multiply(width):
     a = 0
     for i in range(width-2,0,-2):
          a +=1     
          print((a*" ")+"*"+(" "*i)+"*")
     vertical_line((width//2)+1,1)
     for i in range(1,width-1,2):
          print((a*" ")+"*"+(" "*i)+"*")
          a -= 1
#division
def division(width):
     for i in range(width-1,-1,-1):
          print ((" "*i)+"*")

#Part 4
#Function for check answer 
def check_answer(a,b,c,s):
    answer = False
    if s == "+":
        if a+b==c:
            answer = True
    elif s == "-":
        if a-b==c:
            answer = True
    elif s == "*":
        if a*b==c:
            answer = True
    elif s == "/":
        if a/b==c:
            answer = True
          
    return answer




    


    


