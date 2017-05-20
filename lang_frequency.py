import os
import re
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as text:
            return text.read()


def get_most_frequent_words(text):
    found_words = re.findall(r'\b\w+', text)
    quantity_of_duplicate_words = Counter(found_words).most_common(10)
    return quantity_of_duplicate_words


def output_duplicate_words(quantity_of_duplicate_words):
    print('List of repeated words: ')
    for word_repeats in quantity_of_duplicate_words:
        word = word_repeats[0]
        repeat_quantity = word_repeats[1]
        print("Word '%s' repeated %d times." % (word, repeat_quantity))


if __name__ == '__main__':
    filepath = input('Please enter way to txt file: ')
    if os.path.exists(filepath):
        text = load_data(filepath)
        output_duplicate_words(get_most_frequent_words(text))
    else:
        print('File not exist! Check way to file.')
