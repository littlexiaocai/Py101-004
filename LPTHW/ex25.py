def break_words(stuff):
    """ prints the last word after popping it off."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print word

def print_lastJ_word(words):
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


cc = "i test once"

print break_words(cc)

