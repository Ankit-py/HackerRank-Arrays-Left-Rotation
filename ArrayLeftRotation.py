def array_left_rotation(int_list, shift):
    pairs = new_index_value_pairs(int_list, shift)
    replace_int_list(int_list, pairs)
    print(*int_list, sep=' ')

def new_index_value_pairs(int_list, shift):
    return [((index - shift) % len(int_list), value) for index, value in enumerate(int_list)]

def replace_int_list(int_list, pairs):
    for index, value in pairs:
        int_list[index] = value


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    _, shift = map(int, input().strip().split())
    int_list = list(map(int, input().strip().split()))
    array_left_rotation(int_list, shift)
