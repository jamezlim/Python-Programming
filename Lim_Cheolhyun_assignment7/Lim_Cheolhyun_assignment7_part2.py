#Part 2a
name = input ("Name:")
name = name.lower()
name = name.replace(" ","")
reduction = 0
new_name = name 

for c in new_name:
    if c.isalpha() == False:
        name = name.replace(c,"")
        
print ("Your 'cleaned up' name is:",name)
for i in name:
    x = ord(i)-96
    reduction += x
print ("Reduction:",reduction)


#Part 2b
personality = ""
while True:
    if reduction == 0 :
        personality = "emptiness, nothingness, blank"
        break
    elif reduction == 1:
        personality = "independence, loneliness, creativity, originality, dominance, leadership, impatience"
        break
    elif reduction == 2:
        personality = "quiet, passive, diplomatic, co-operation, comforting, soothing, intuitive, compromising, patient"
        break
    elif reduction == 3:
        personality = "charming, outgoing, self expressive, extroverted, abundance, active, energetic, proud"
        break
    elif reduction == 4:
        personality = "harmony, truth, justice, order discipline, practicality"
        break
    elif reduction == 5:
        personality = "new directions, excitement, change, adventure"
        break
    elif reduction == 6:
        personality = "love, harmony, perfection, marriage, tolerance, public service"
        break
    elif reduction == 7:
        personality = "spirituality, completeness, isolation, introspection"
        break
    elif reduction == 8:
        personality = "organization, business, commerce, new beginnings"
        break
    elif reduction == 9:
        personality = "romatic, rebellious, determined, passionate, compassionate"
        break
    elif reduction == 11:
        personality = "idealism, visionary, inspirational"
        break
    elif reduction == 12:
        personality = "perfectionist, discriminating"
        break
    elif reduction == 22:
        personality = "builder, leader, humanitarian, practical, honest"
        break


    # Too big to clasify into given reduction numbers
    reduction = str(reduction)
    total = 0
    for digits in reduction:
        total += int(digits)
    reduction = total 
    print ("Reduction:",reduction) 
    continue 
print ("Your name reduces to ...",reduction,"-",personality,"!")       

    

