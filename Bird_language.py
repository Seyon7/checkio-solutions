VOWELS = "aeiouy"

def translate(phrase):
    result = ''
    phrase_lst = list(phrase)

    for i in range(len(phrase) - 1):
        if phrase_lst[i] not in VOWELS and phrase_lst[i] != ' ':
            phrase_lst[i+1] = ''
    for j in range(len(phrase) - 2):
        if phrase_lst[j] == phrase_lst[j+1] and phrase_lst[j] == phrase_lst[j+2]:
            phrase_lst[j+1] = ''
            phrase_lst[j+2] = ''

    for _ in phrase_lst:
        if _ != '':
            result = result + _
    return result


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))
    print(translate("hoooowe yyyooouuu duoooiiine"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
