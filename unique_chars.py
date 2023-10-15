# Determine if a string has all unique characters

def is_chars_unique(word):
    found = {}
    for char in word:
        if char in found:
            return False
        found[char] = True

    return True

example = 'abcab'
print(is_chars_unique(example))
