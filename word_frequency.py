# count frequency of a given word in a book. What is multiple times? pre-compute
# Assume case insensitive.

book_raw = 'Once upon a time there was a cat named Puddles. This cat was very cat like. He was a crazy cat.'

class Book:
    def __init__(self, book):
        self._book = book

        word_counts = {}
        for w in book.split(' '):
            w = w.lower()
            clean_word = []
            for char in w:
                if char.isalnum():
                    clean_word.append(char)
            clean_word = ''.join(clean_word)
            if clean_word in word_counts:
                word_counts[clean_word] += 1
            else:
                word_counts[clean_word] = 1

        self._word_counts = word_counts

    def count_word(self, word):
        return self._word_counts.get(word, 0)

book = Book(book_raw)
print(book.count_word('a'))
