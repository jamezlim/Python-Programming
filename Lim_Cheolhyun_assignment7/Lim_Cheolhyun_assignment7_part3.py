#Part 3a 
import random

def random_letter():
    random_letter = ""
    lower_or_upper = random.randint(1,2)
    lower = random.randint(97,122)
    upper = random.randint(65,90)
    if lower_or_upper == 1:
        random_letter = chr(lower)
    elif lower_or_upper == 2:
        random_letter = chr(upper)
    return random_letter

def random_letter_combination(num):
    random_letter_combination = ""
    for i in range (1,num+1):
        random_letter_combination += random_letter()
    return random_letter_combination
        
def add_letters(word,num):
    generated_word = ""
    for c in word:
        generated_word += c + random_letter_combination(num)
    return generated_word    

def remove_letters(word,num):
    original_word = ""
    for c in word [0: :num+1]:
        original_word += c
    return original_word 

def shift_characters(word,num):
    new_word = ""
    for c in word :
        new_word += chr(ord (c) + num)
    return new_word

#Part 3b
response = input ("(e)ncode, (d)ecode or (q)uit:")
if response == "e":
    num = int(input ("Enter a number between 1 and 5:"))
    while num >5 and num < 1:
        print ("Sorry, that's not a number between 1 and 5")
        num = input ("Enter a number between 1 and 5:")
    phrase = input ("Enter a phrase to encode:")
    word = add_letters (phrase, num)
    code_word = shift_characters(word,num)
    print ("Your encoded word is:",code_word)
        
elif response == "d":
    num = int(input ("Enter a number between 1 and 5:"))
    while num >5 and num < 1:
        print ("Sorry, that's not a number between 1 and 5")
        num = input ("Enter a number between 1 and 5:")
    phrase = input("Enter a phrase to decode:")
    word = remove_letters(phrase,num)
    decoded_word = shift_characters(word,-num)
    print ("Your decoded word is:",decoded_word)
else :
    print ("Thank You")
            
