import time
import random

with open('WikiQA-train.txt','r') as file:
    data = file.read()

def total_next_outcomes(data, prompt):
    data_list_relationships = data.split()
    loop = 0

    next_words = []

    while loop < len(data_list_relationships):
        if data_list_relationships[loop] == prompt:
            if (loop + 1) == len(data_list_relationships):
                next_word_index = 0
                next_words.append(data_list_relationships[next_word_index])
            else:
                next_word_index = loop + 1
                next_words.append(data_list_relationships[next_word_index])
        loop += 1

    return next_words


def probable_next_word(possible_words):
    word_count = {}

    for word in possible_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    #print(word_count)
    return word_count


def most_probable_word(word_count):
    values = list(word_count.values())
    is_probability_same = all(x == values[0] for x in values)

    if is_probability_same:
        return random.choice(list(word_count.keys()))
    else:
        highest_count = 0
        most_probable_word = ""

        for key, value in word_count.items():
            if value > highest_count:
                highest_count = value
                most_probable_word = key
        
        return most_probable_word


prompt = input("Prompt: ")

while True:
    try:
        possible_words = total_next_outcomes(data, prompt)

        word_count = probable_next_word(possible_words)

        next_word = most_probable_word(word_count)
        time.sleep(1)
        print(next_word)
        if next_word.endswith("."):
            break
        prompt = next_word

    except:
        break