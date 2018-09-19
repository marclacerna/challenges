from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        dic_val = [line.strip('\n') for line in f]
    return dic_val


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = [LETTER_SCORES[i.upper()] for i in word if i.isalpha()]

    return sum(score)


def max_word_value(*args):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    dic_val = load_words() if len(args) == 0 else [i for i in args[0]]
    score_name_dic = {calc_word_value(i): i for i in dic_val}

    return score_name_dic[max(score_name_dic)]


if __name__ == "__main__":
    pass  # run unittests to validate
