def frequency_sort(items: list) -> list:
    rez = []
    while True:
        freq = 0
        elem = None
        for i in items:
            if i not in rez:
                curr_freq = items.count(i)
                if curr_freq > freq:
                    freq = curr_freq
                    elem = i
        for j in range(freq):
            rez.append(elem)
        if len(rez) == len(items):
            break
    return rez


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'alex', 'alex', 'carl']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
