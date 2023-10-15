# check permutations, 2 strings, check if one is permutation of another. Permutations is chars rearanged.

def set_char_counts(char, chars, str_index):
    if char not in chars:
        chars[char] = [0, 0]
    chars[char][str_index] += 1

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    chars = {} # char : (str1_count, str2_count)

    for char in str1:
        set_char_counts(char, chars, 0)

    for char in str2:
        set_char_counts(char, chars, 1)

    for counts in chars.values():
        if counts[0] != counts[1]:
            return False

    return True


print(is_permutation('cbadn', 'abdcm'))
