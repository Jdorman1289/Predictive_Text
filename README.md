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


https://github.com/user-attachments/assets/a4554877-dd85-4c5a-9c4e-6f06ffcf4cc8


## Demo




