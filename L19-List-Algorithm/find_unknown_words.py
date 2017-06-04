def find(list, name):
    for index in range(len(list)):
        if list[index] == name:
            return index
    return -1

#2
vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

def find_unknown_words(vocab, words):
    result = []
    for w in words:
        if find(vocab, w) == -1:
            result.append(w)
    return result

print(find_unknown_words(vocab, book_words))
