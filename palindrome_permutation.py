
def is_palindrome_permutation(word):
    #todo handle spaces, ignore
    char_count = {}
    for c in word:
        if c == ' ':
            continue

        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    odd_found = False # if more than one odd found, not a palindrome

    for counts in char_count.values():
        if counts % 2 == 0:
            continue
        elif odd_found:
            return False
        else:
            odd_found = True

    return True

print(is_palindrome_permutation('aacbb cd'))
