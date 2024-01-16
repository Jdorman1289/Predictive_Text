# Text Generation with N-Grams in Shakespeare's Works

This API generates text based on Shakespeare's works using an N-gram model.

## How it Works

- The API reads the text of Shakespeare's works and stores it in a variable called `data`.
- The function `total_next_outcomes` takes the `data` and a prompt as input and returns a dictionary of the next words and their frequency of appearance in the data, given the prompt.
- The function `most_probable_word` takes the dictionary of the next words and their frequency of appearance and returns the next word with the highest frequency.

## Usage

To run the API, type the following command in the terminal:

```
uvicorn generate:app --reload
```

## Note

The script uses a pre-existing file named `shakespeare_set.txt`, which contains the text of Shakespeare's works. Make sure the file is in the same directory as the script.

## Demo


https://github.com/Jdorman1289/Predictive_Text/assets/103331059/55acbf3d-6f08-4fac-9caa-e0f81d94696d

