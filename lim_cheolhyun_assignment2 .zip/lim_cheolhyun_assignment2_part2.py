#Part 2 Grade Calculator
#Basic Info
name = input("What is your name?")
class_name = input ("What class are you in?")
print ()
weighting_of_tests = float(input ("How much are tests worth in this class? (i.e. 0.40 for 40%)"))

#Test scores 
test_1 = int(input ("Enter test score #1"))
test_2 = int(input ("Enter test score #2"))
test_3 = int(input ("Enter test score #3"))
print ()

#Test Avg
test_avg = (test_1 + test_2 + test_3)/3
test_avg_2 = float ( format(test_avg,".2f"))
print("Your test average is:", test_avg_2)
print ()

#HW scores and weighting
weighting_of_hw = float (input ("How much are homework assignments worth in this class? (i.e. 0.60 for 60%)"))
hw_1 = int( input ("Enter homework score #1"))
hw_2 = int( input ("Enter homework score #2"))
hw_3 = int( input ("Enter homework score #3"))

#Hw Avg
hw_avg = (hw_1 + hw_2 + hw_3)/3
hw_avg_2 = float (format(hw_avg,".2f"))
print ()
print ("Your homework average is:", hw_avg_2)

#Final Avg
final_score = ((weighting_of_tests * test_avg_2) + (weighting_of_hw * hw_avg_2))/2
final_score_2 = float( format(final_score, ".2f")) 
print ()
print ("Thanks,",name,"Your final score in", class_name,"is", final_score)

#Basically, the final score is the weight of each category times each category summed up divided by two
#Some of the average numbers you need to use the format operator to make them two decimal places and after that make them a float


