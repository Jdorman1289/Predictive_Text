import random

context_words = [] 

with open('shakespeare_set.txt','r') as file:
    data = file.read()

def total_next_outcomes(data, prompt):
    data_list_relationships = data.split()
    combo_size = len(prompt.split())

    next_words = {}

    for i in range(len(data_list_relationships) - combo_size + 1):
        if ' '.join(data_list_relationships[i:i+combo_size]) == prompt:
            if i + combo_size < len(data_list_relationships):
                next_word = data_list_relationships[i + combo_size]
                if next_word in next_words:
                    next_words[next_word] += 1
                else:
                    next_words[next_word] = 1
    # print(len(next_words))
    return next_words

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
        next_words = total_next_outcomes(data, prompt)
        next_word = most_probable_word(next_words)

        if context_words[-3:] == context_words[-6:-3] and (len(context_words)) != 0:
            next_word = (next_word) + '.'
            context_words.append(next_word)
        else:
            context_words.append(next_word)

        if next_word.endswith(".") or next_word.endswith("?") or next_word.endswith("!"):
            break

        print('*' * len(context_words))

        prompt = ' '.join(context_words)

    except IndexError:
        print("IndexError")
        break
    
print(' ...' + ' '.join(context_words))
