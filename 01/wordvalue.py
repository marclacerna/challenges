from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return [line.strip('\n') for line in f]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[i.upper()] for i in word if i.isalpha()])


def max_word_value(args=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if args is None:
        args = load_words()

    return max(args, key=calc_word_value)


if __name__ == "__main__":
    pass  # run unittests to validate
