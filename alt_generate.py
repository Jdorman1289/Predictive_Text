import random

# list to store generated text
context_words = []

# open and read the file containing training data
with open('shakespeare_set.txt','r') as file:
    data = file.read()

# function to get a dictionary of possible next words and their count after the prompt
def total_next_outcomes(data, prompt):
    # split the data into a list of words
    data_list_relationships = data.split()
    # size of n-gram
    combo_size = len(prompt.split())

    # dictionary to store possible next words and their count
    next_words = {}

    # loop over the data to get the next words after the prompt
    for i in range(len(data_list_relationships) - combo_size + 1):
        if ' '.join(data_list_relationships[i:i+combo_size]) == prompt:
            if i + combo_size < len(data_list_relationships):
                next_word = data_list_relationships[i + combo_size]
                if next_word in next_words:
                    # increment the count if the next word is already in the dictionary
                    next_words[next_word] += 1
                else:
                    # add the next word to the dictionary with count 1
                    next_words[next_word] = 1
    return next_words

# function to get the most probable next word from the dictionary of next words and their count
def most_probable_word(word_count):
    values = list(word_count.values())
    # check if all values are equal
    is_probability_same = all(x == values[0] for x in values)

    if is_probability_same:
        # if all values are equal, return a random word from the keys
        return random.choice(list(word_count.keys()))
    else:
        highest_count = 0
        most_probable_word = ""

        # loop over the dictionary to get the word with the highest count
        for key, value in word_count.items():
            if value > highest_count:
                highest_count = value
                most_probable_word = key

        # return the word with the highest count
        return most_probable_word

# get the initial prompt from the user
prompt = input("Prompt: ")

# loop to generate text continuations
while True:
    try:
        # get the dictionary of next words and their count
        next_words = total_next_outcomes(data, prompt)
        # get the most probable next word
        next_word = most_probable_word(next_words)

        # if the last 3 generated words are equal to the 3 words before them,
        # add a period to the next word to end the text
        if context_words[-3:] == context_words[-6:-3] and (len(context_words)) != 0:
            next_word = (next_word) + '.'
            context_words.append(next_word)
        else:
            context_words.append(next_word)

        # if the next word ends with a period, question mark, or exclamation mark, break the loop
        if next_word.end
        break

    # Print asterisks to indicate the length of context_words
    print('*' * len(context_words))

    # Join the list of context_words into a single string to use as the next prompt
    prompt = ' '.join(context_words)

# If an IndexError occurs, print "IndexError" and break out of the loop
except IndexError:
    print("IndexError")
    break



'''
read starter paragraph from file
store individual words.
	for every WORD, find and store all words that follow each instance of that WORD.
		store as key:value pair.
			Ex: String = "Hey you, how are you doing?!"
			dict of key/value pairs: [
				hey: [you]
				you: [how, doing]
				how: [are]
				are: [you]
				doing: [set to Null as no words followed]
				]
		
count how many times a 'value' appears after a key
	String = "The fox was brown. The fox is quick."
	kvpairs_dict = [
		the: [fox, fox],
			fox_value_count = 2
		fox: [was, is],
			was_value_count = 2
			is_value_count = 1
		was: [brown],
			brown_value_count = 2
		brown: [the],
			the_value_count = 2
		is: [quick],
			quick_value_count = 2
		quick: [Null]
		]

create weights for kvpairs
	for each key:
		count total number of values (AKA words that followed the 'key' word)
		Ex: kvpairs_dict = [
			.... ,
			the: [fox, fox, boy, girl, quick, log],
			... ,
			]
		# WORD_value_count = len(dict.WORD[# OF VALUES ASSOCIATED WITH WORD])
		THE_value_count == 6

'''
