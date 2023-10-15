# replace spaces in a string with %20

def shift_array_2_places(lst):
    new_list = lst.copy()
    for i in range(len(new_list)-1, -1, -1):
        while len(new_list) <= i+2:
            new_list.append('')
        new_list[i+2] = new_list[i]

    new_list[0] = ''
    new_list[1] = ''
    return new_list


def urlify(string: str):
    str_list = list(string)
    for i, char in enumerate(str_list):
        if char == ' ':
            # shift positions over by 2
            str_list = str_list[0:i+1] + shift_array_2_places(str_list[i+1:])
            str_list[i] = '%'
            str_list[i+1] = '2'
            str_list[i+2] = '0'
    print(str_list)
    return ''.join(str_list)



print(urlify('hello world this is me'))
