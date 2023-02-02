import time
import random

data = "First, the data confirms that our average number of heads does approach what probability suggests it should be. Furthermore, this average improves with more trials. In 10 trials, there's some slight error, but this error almost disappears entirely with 1,000,000 trials. As we get more trials, the deviation away from the average decreases. Sound familiar? Sure, we could have flipped the coin ourselves, but Python saves us a lot of time by allowing us to model this process in code. As we get more and more data, the real-world starts to resemble the ideal."

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
    is_same = all(x == values[0] for x in values)

    if is_same:
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
        prompt = next_word

    except:
        break