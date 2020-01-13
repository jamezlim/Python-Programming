# Part 3: Data Size Converter 
file_size = int (input ("Enter file size in Kilobytes (KB)"))
print (file_size,"KB...")
print ()

# File size into bit, byte, megabytes, gigabytes 
c = file_size * (1024 * 8)
bit = format (c,',.2f')


v = file_size * 1024
byte = format (v,',.2f')


x = file_size / 1024
mega = format (x, ',.2f')


y = file_size / (1024 * 1024)
giga = format (y, ',.2f')

# Printing out and formatting 
q = format ("... in bits", '<20s')
w = format (bit,'>20s')
print (q,w,"bits")

e = format ("... in bytes", '<20s')
r = format (byte,'>20s') 
print (e,r,"bytes")

t = format ("... in megabytes", '<20s')
u = format (mega,'>20s')
print (t,u,"MB")
i = format ("... in gigabytes", '<20s')
o = format (giga,'>20s')
print (i,o,"GB")

# You want to convert your file size and by using the format operator make them two decimal points
# An important thing to note is that using the format operator the program will give the user
# a string. Finally you format and print the converted values using "<20s",">20s"

#syntax Errors q = format ("...in bits",<20s)
#              print (q,w,"bits"

#Runtime Errors x = 7
#               y = 0
#               print (x / y )
#Logic Errors c (bits) = file_size / (1024 * 8)
#             y (giga) = file_size * (1024 * 1024)  
