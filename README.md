# Text Generation with N-Grams in Shakespeare's Works

This script is used to generate text based on Shakespeare's works using an N-gram model.

## How it Works

- The script reads in the text of Shakespeare's works and stores it in a variable `data`.
- The function `total_next_outcomes` takes the `data` and a prompt as input and returns a dictionary of next words and their frequency of appearance in the data, given the prompt.
- The function `most_probable_word` takes the dictionary of next words and their frequency of appearance and returns the next word with the highest frequency.

## Usage

To run the script, type the following command in the terminal:

```
python generate.py
```

And enter the prompt when prompted. The generated text will be displayed at the end.

## Note

The script uses a pre-existing file named `shakespeare_set.txt`, which contains the text of Shakespeare's works. Make sure the file is in the same directory as the script.
