import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Prompt(BaseModel):
    text: str

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/suggest/")
async def suggest_next_word(prompt: Prompt):
    try:
        # open and read the file containing training data
        with open('shakespeare_set.txt', 'r') as file:
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
                if ' '.join(data_list_relationships[i:i + combo_size]) == prompt:
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

        next_words = total_next_outcomes(data, prompt.text)
        next_word = most_probable_word(next_words)
        return {"next_word": next_word}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
