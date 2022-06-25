import pickle
import gzip
from math import log2


def compare(prim, test):
    # prim is the primary words and test is the words we test against prim
    # return a 5 letter string, representing the output according to wordle rules
    result = "-----"

    for i in range(5):
        color = ''
        if prim[i] == test[i]:  # GREEN
            color = 'G'
            prim = prim[:i] + '-' + prim[i+1:]
        elif test[i] in prim:  # YELLOW
            color = 'Y'
            index = prim.index(test[i])
            prim = prim[:index] + '-' + prim[index+1:]
        elif test[i] not in prim:  # GRAY
            color = 'W'
        result = result[:i] + color + result[i+1:]

    return result


def get_score(word, words):
    score = 0
    my_dict = {}
    for w in words:
        if compare(word, w) in my_dict:
            my_dict[compare(word, w)] += 1
        else:
            my_dict[compare(word, w)] = 1

    for val in my_dict.values():
        p = val/len(words)
        score += p*(-log2(p))

    return score


def rate_words(words):
    rated_words = [(w, get_score(word=w, words=words))
                   for w in words]
    rated_words.sort(key=lambda c: c[1], reverse=True)
    return list(map(lambda x: x[0], rated_words))


def filter_words(words, guess, result):
    new_words = [w for w in words if compare(w, guess) == result]
    return new_words


def get_words():
    words = []
    with open('valid_words.txt', 'r') as finput:
        words = finput.readline().split(' ')
    return words


def take_input():
    res = ''
    while True:
        res = input('result: ').upper()
        if all([c in 'GWY' for c in res]) == True and len(res) == 5:
            break
        print('Wrong input, try again.')
    return res


def main():
    words = get_words()

    for turn in range(1, 7):
        if len(words) == 0:
            print('error occured: no word found')
            break

        guess = words[0]
        print('current guess: ' + guess +
              '\t\t(other possible words: '+str(len(words)-1)+')')
        result = take_input()
        if result == 'GGGGG':
            print('yayy!')
            break
        words = filter_words(words=words, guess=guess,result=result)
        words = rate_words(words)
        if turn == 6:
            print('failed :(')


if __name__ == "__main__":
    main()
