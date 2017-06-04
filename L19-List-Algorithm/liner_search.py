def find(list, name):
    for index in range(len(list)):
        if list[index] == name:
            return index
    return -1

def find_unknown_words(vocab, words):
    result = []
    for w in words:
        if find(vocab, w) == -1:
            result.append(w)
    return result

def load_words_from_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    words = content.split()
    return words

bigger_vocab = load_words_from_file("vocab.txt")
print("There are ", len(vocab), "words in the vocabulary, starts with ", vocab[0:6])

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

book_words = get_words_in_book("alice_in_wonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))

import time

t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
