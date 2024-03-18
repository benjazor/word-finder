import os

language = "en"  # "fr"


def match_pattern(pattern: str, word: str):
    if len(pattern) != len(word):
        return False
    for i, char in enumerate(pattern):
        if char != "_" and char != word[i]:
            return False
    return True


def read_file(file_path: str):
    with open(file_path, "r") as file:
        return file.readlines()


def input_list(prompt: str = "Enter a list:"):
    print(prompt)
    lst = []
    while True:
        item = input()
        if item in {"", " ", "continue"}:
            break
        if len(item) > 1:
            print("Please enter only one letter at a time.")
            continue
        lst.append(item)
    return lst


def main():
    sorted_dict = read_file(os.path.join("dict", language, "dict_sorted.csv"))
    no_accent_dict = read_file(os.path.join("dict", language, "dict_no_accent.csv"))

    illegal_letters = input_list("Enter the illegal letters:")
    required_letters = input_list("Enter the required letters:")

    pattern = input("Enter the pattern: ")

    # Find matching words in the dictionary
    matching_words = set()
    for i, word in enumerate(sorted_dict):
        if match_pattern(pattern, no_accent_dict[i].strip()):
            matching_words.add(word.strip())

    # Filter out words with illegal letters and without required letters
    filtered_matching_words = set()
    for word in matching_words:
        matching = not any(letter in word for letter in illegal_letters) and all(
            letter in word for letter in required_letters
        )
        if matching:
            filtered_matching_words.add(word)

    print(f"Matching words: {filtered_matching_words}")


if __name__ == "__main__":
    main()
