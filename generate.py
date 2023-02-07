import random
import time
import os

# list to store generated text
context_words = []

# open and read the file containing training data
with open('shakespeare_set.txt','r') as file:
    data = file.read()

# Print iterations progress
def print_progress_bar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', print_end = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = print_end)
    # Print New Line on Complete
    if iteration == total: 
        print()

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
    # print(len(next_words))
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
reference_prompt = prompt

# loop to generate text continuations
while True:
    try:
        # get the dictionary of next words and their count
        next_words = total_next_outcomes(data, prompt)
        # get the most probable next word
        next_word = most_probable_word(next_words)
 
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{reference_prompt} " + ' '.join(context_words))


        is_keeping = input(f"suggested word: '{next_word}'\n\nPress 1 to keep or 2 to change. ")
        if is_keeping == '1':
            context_words.append(next_word)

            # Join the list of context_words into a single string to use as the next prompt
            prompt = ' '.join(context_words)
        else:
            prompt = input("Enter the next word: ")
            context_words.append(prompt)

        
        if context_words[-1] == '.' or context_words[-1] == '!' or context_words[-1] == '?':
            is_done = input("\n\nWould you like to continue? Press 1 to continue or 2 to end.\n")
            if is_done == '1':
                prompt = input("Prompt: ")
            else:
                break

        # A List of Items
        items = context_words
        l = len(items)

        # Initial call to print 0% progress
        print_progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i, item in enumerate(items):
            time.sleep(0.1)
            # Update Progress Bar
            print_progress_bar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    # If an IndexError occurs, print "IndexError" and break out of the loop
    except IndexError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{reference_prompt} " + ' '.join(context_words))
        quit_on_shakespeare = input("\nShakespeare has no suggestions for that. Would you like to continue? Press 1 to continue or 2 to end. ")
        if quit_on_shakespeare == '1':
            prompt = input("Prompt: ")
            context_words.append(prompt)
        else:
            break

# print the generated text
print("\nGenerated Text:\n")    
print(f"{reference_prompt} " + ' '.join(context_words))
