def flat_list(array):
    rez = []
    for i in array:
        if type(i) != list:
            rez = rez + [i]
        else:
            rez = rez + flat_list(i)
    return rez

if __name__ == '__main__':
    print(flat_list([1, [2, 2, 2], 4]))
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')