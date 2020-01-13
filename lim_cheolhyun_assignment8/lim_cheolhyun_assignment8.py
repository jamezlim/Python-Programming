file = input ("What file would you like to open?")

# Opening user file/reading/closing
file_object = open(file,"r")
full_text = file_object.read()
file_object.close()

# Converting full text to lower case then making to list 
small_full_text = full_text.lower()
full_text_list = small_full_text.split(" ")

# Remove unnecessary symbols from the list of all the words in the text 
clean_text_list = []
for words in full_text_list:
    clean_word = words.strip(".")
    cleaner_word = clean_word.strip(",")
    clean_text_list.append(cleaner_word)

words = input("What words would you like to search for?")

# Converting search words with commas into list without spaces 
small_words = words.lower()
word_list = small_words.split(",")
clean_word_list = []
for word in word_list:
    clean_word = word.strip(" ")
    clean_word_list.append(clean_word)

print("\n... analyzing ... hold on ... \n")
print ("Frequency of word usage within", file + ":")

# Building an accumulator and finding search words from list of all the words in the text 
for words in clean_word_list:
    #["  ","  ","  "]
    
    count = 0
    for text in clean_text_list:
        if words == text:
            count += 1
    print ("   ",format(words,'<15s'),format("/",'>10s')," ",count,"occurences")
    
