#Part1
while True:
    file_root = input ("Enter a class file to grade (i.e. class1 for class1.txt):")
    file = file_root + ".txt"
    try:
        file_object = open (file,"r")
        data = file_object.read()
        file_object.close()
        print ("Successfully opened",file)
        print()
        break
        
    except:
        print ("File cannot be found\n")

#Part2       
# Answers made into a list        
answers = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_list = answers.split(",")

# data = "N0000000,A,B,....,N0000000,C,D"
# break data according to student
student_data = data.split("\n")

# student_data = ["N000001,A,B...D","N000002,B,C....D"]
number_of_students = len(student_data)

invalid_lines = 0
score_total = 0
student_score_list = []
net_id_list = []
for each_student in student_data:
    each_student_answer = each_student.split (",")
    # each_student_answer = ["N000001","A","B"..."A","D"]
    # each_student = "N00001,A,B...D"
    # checking for un-usable line
    length = len(each_student_answer)
    if length != 26:
        invalid_lines += 1
        continue

    question_number = 0
    score = 0
     
    for correct_answer in answer_list  :    
    #print("DEBUGGING: ", student_answer)

        answer= each_student_answer[question_number+1]
    
        question_number +=1

    

        if answer == correct_answer:
            score += 4
        elif answer == '':
            continue 
        else:
            score -= 1

    score_total += score
    student_score_list.append(score)
    net_id_list.append(each_student_answer[0])

# each_student_answer = ["N000001","A","B"..."A","D"]
# answer_list = ["B","A"....,"D","D"]

mean = score_total/ number_of_students
mean = format(mean,".2f")

print ("Grade Summary:")
print ("Total students:", number_of_students)
print ("Unusable lines in the file:", invalid_lines)
print ("Highest score:", max(student_score_list))
print ("Lowest score:", min(student_score_list))
print ("Mean score:", mean)


# Part 3
# Median
old_score_list = student_score_list.copy()
student_score_list.sort()

# if even --> average of two middle values 
if number_of_students % 2 == 0:
    x = number_of_students//2
    median = (student_score_list[x]+ student_score_list[x+1])/2
# if odd --> middle value    
else:
    x = number_of_students//2
    median = student_score_list[x]

# Mode
mode = 0 
max_value = 0 
for scores in student_score_list:
    occurance = student_score_list.count(scores)
    if occurance > max_value:
        max_value = occurance
        mode = score 

# Range
range_difference = max(student_score_list)- min(student_score_list)

print ("Meadian:", median)
print ("Mode:", mode)
print ("Range:", range_difference)


# Part 4 and 5
new_file = file_root +"_grades.txt"
file_object = open (new_file,"w")

user_answer = input ("Would you like to curve the exam? 'y' or 'n':")

if user_answer == "y":
    user_mean = int(input ("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0):"))
    while user_mean < 0:
        print ("Invalid curve, try again.\n")
        user_mean = int(input ("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0):"))
    print("Done! Check your grade file!")
                           
else:
    print("Done! Check your grade file!")

for i in range(0,len(student_score_list)):
    net_id = net_id_list[i]
    decimal_score = format (old_score_list[i],".2f")
    y = float(decimal_score)
    file_object.write(net_id)
    file_object.write(",")
    file_object.write(decimal_score)
    if user_answer == "y":
        difference = user_mean - y
        new_score = str(y + difference)
        file_object.write(",")
        file_object.write(new_score)
    file_object.write("\n")
file_object.close()
