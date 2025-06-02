from nltk.corpus import words

def get_word_list():
    return [w.lower() for w in words.words() if len(w) == 5 and w.isalpha()]