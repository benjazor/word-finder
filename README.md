# Word Finder

This is a Python script that finds words from a dictionary that match a given pattern, don't contain any illegal letters, and do contain all required letters.

## Usage

1. Run the script with Python `python3 finder.py`.
2. When prompted, enter the illegal letters one at a time. These are the letters that you don't want to appear in the words. Press enter after each letter. When you're done, enter "continue".
3. Next, enter the required letters one at a time. These are the letters that you want to appear in the words. Press enter after each letter. When you're done, enter "continue".
4. Finally, enter the pattern. This is a string of characters where each character represents a letter in the word. Use an underscore (_) to represent unknown letters. Example pattern for a 5-letter word starting with "a" and ending with "e": "a___e".

The script will then print out the words from the dictionary that match the pattern, don't contain any of the illegal letters, and do contain all of the required letters.

## Requirements

- Python 3.6 or higher
