import re
from collections import Counter


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='UTF-8') as text:
            return text.read()
    except Exception:
        print('Error! Please check way to file and load correct file!')


def get_most_frequent_words(text):
    found_words = re.findall(r'\b\w+', text)
    quantity_of_words = Counter(found_words).most_common(10)
    print('List of repeated words: ')
    for word_repeats in quantity_of_words:
        word = word_repeats[0]
        repeat_quantity = word_repeats[1]
        print("Word '%s' repeated %d times." % (word, repeat_quantity))


if __name__ == '__main__':
    filepath = input('Please enter way to txt file: ')
    text = load_data(filepath)
    if text:
        get_most_frequent_words(text)
