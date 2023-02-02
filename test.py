data = "First, the data confirms that our average number of heads does approach what probability suggests it should be. Furthermore, this average improves with more trials. In 10 trials, there's some slight error, but this error almost disappears entirely with 1,000,000 trials. As we get more trials, the deviation away from the average decreases. Sound familiar? Sure, we could have flipped the coin ourselves, but Python saves us a lot of time by allowing us to model this process in code. As we get more and more data, the real-world starts to resemble the ideal."

prompt = input("Prompt: ")

def total_next_outcomes(data, prompt):
    data_list_relationships = data.split()
    loop = 0

    next_words = []

    while loop < len(data_list_relationships):
        if data_list_relationships[loop] == prompt:
            next_word_index = loop + 1
            next_words.append(data_list_relationships[next_word_index])
        loop += 1

    return next_words

possible_words = total_next_outcomes(data, prompt)

