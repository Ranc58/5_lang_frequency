import re
from collections import Counter


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='UTF-8') as text:
            return text.read()
    except Exception:
        print('Error! Please check way to file and load correct file!')


def get_most_frequent_words(text):
    result = re.findall(r'\b\w+', text)
    quantity_of_words = Counter(result).most_common(10)
    print('List of repeated words: ')
    for word in quantity_of_words:
        word_1 = word[0]
        value = word[1]
        print("Word '%s' repeated %d times." % (word_1, value))


if __name__ == '__main__':
    filepath = input('Please enter way to txt file: ')
    text = load_data(filepath)

