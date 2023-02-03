import random
from itertools import combinations

context_words = [] 

data = """Improving the robustness of machine learning models for natural language tasks has become a major artificial intelligence topic in recent years. Large language models have always been one of the most trending areas in AI research, backed by the rise of generative AI and companies racing to release architectures that can create impressively readable content, even computer code. Language models have traditionally been trained using online texts from sources such as Wikipedia, news stories, scientific papers and novels. However, in recent years, the tendency has been to train these models on increasing amounts of data in order to improve their accuracy and versatility. But, according to a team of AI forecasters, there is a concern on the horizon: we may run out of data to train them on. Researchers from Epoch emphasize in a study that high-quality data generally used for training language models may be depleted as early as 2026. As developers create more sophisticated models with superior capabilities, they must gather more texts to train them on, and LLM researchers are now increasingly concerned about running out of quality data. A principal research scientist in the MIT Information and Decision Systems laboratory and leader of the lab's Data-to-AI group, may have found the solution. In a paper on Rewrite and Rollback R&R: Metric-Guided Adversarial Sentence Generation recently published in the findings of 2022, the proposed framework can tweak and turn low-quality data from sources such as Twitter and 4Chan into high-quality data such as that from sources with editorial filters, such as Wikipedia and industry websites, increasing the amount of the correct type of data to test and train language models on. First, the data confirms that our average number does approach what probability suggests it should be. Furthermore, this average improves with more trials. In 10 trials, there's some slight error, but this error almost disappears entirely with 1,000,000 trials. As we get more trials, the deviation away from the average decreases. Sound familiar? Sure, we could have flipped the coin ourselves, but Python saves us a lot of time by allowing us to model this process in code. As we get more and more data, the real-world starts to resemble the ideal."""

# with open('WikiQA-train.txt','r') as file:
#     data = file.read()

def total_next_outcomes(data, prompt):
    data_list_relationships = data.split()

    combo_size = len(prompt.split())

    data_list_relationships = list(combinations(data_list_relationships, combo_size))
    data_list_relationships = [' '.join(i) for i in data_list_relationships]

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

    # print(word_count)
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
        next_word = next_word.split().pop()

        context_words.append(next_word)

        if next_word.endswith("."):
            break

        # print(' '.join(context_words[-3:]))
        prompt = ' '.join(context_words[-3:])

    except:
        break
    
print(' '.join(context_words))