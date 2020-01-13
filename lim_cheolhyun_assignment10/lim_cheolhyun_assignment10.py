import random
dic = {}

file_object = open("python_asg10_Roget_Thesaurus.txt","r")
data = file_object.read()
data = data.split("\n")
file_object.close
#data = ["key,value,value","key,value,value"]

#Creating the dictionary
for line in data:
    line = line.split(",")
    key = line[0]
    line.pop(0)
    value = line
    dic[key] = value

print("Total words in thesaurus:",len(dic.keys()))
print()
chance = float(input("Enter a % chance to change a word:"))
print()

#Opening text bieber 
file_object = open("bieber_baby.txt","r")
lyrics = file_object.read()
file_object.close()
lyrics = lyrics.split("\n")
# lyrics = ["you know you love me","line","line"...]

#Break into lines and then into words
for line in lyrics:
    line = line.lower()
    line = line.split(" ")
    #line = ["you","know","you","love","me"]
    for word in line:
        word = word.lower()
        if word in dic.keys():
            # val = value between 0 ~ 1 
            val = random.random()
            # between numbers 0 and 1 40% of the values are less than 0.4 
            if val <= chance:
                random_value = random.randint(0,len(dic[word])-1)
                line[line.index(word)] = dic[word][random_value].upper()
    line = " ".join(line)
    print(line)
    


            
            
            



