import pickle
import gzip
from math import log2



def get_score(word, words, dict):
    score = 0
    my_dict = {}
    for w in words:
        if dict[word, w] in my_dict:
            my_dict[dict[word, w]] += 1
        else:
            my_dict[dict[word, w]] = 1

    for val in my_dict.values():
        p = val/len(words)
        score += p*(-log2(p))

    return score


def rate_words(words, dict):
    rated_words = [(w, get_score(word=w, words=words, dict=dict))
                   for w in words]
    rated_words.sort(key=lambda c: c[1], reverse=True)
    return list(map(lambda x: x[0], rated_words))


def get_word_result_dict(words):
    dict = {}
    with gzip.open('dictionary.pklz', 'rb') as f:
        dict = pickle.load(f)
    return dict


def filter_words(words, guess, result, dict):
    new_words = [w for w in words if dict[(w, guess)] == result]
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
    dict = get_word_result_dict(words)

    for turn in range(1, 7):
        if len(words) == 0:
            print('error occured: no word found')
            break

        guess = words[0]
        print('current guess: ' + guess + '\t\t(other possible words: '+str(len(words)-1)+')')
        result = take_input()
        if result == 'GGGGG':
            print('yayy!')
            break
        words = filter_words(words=words, guess=guess,
                             result=result, dict=dict)
        words = rate_words(words, dict=dict)
        if turn == 6:
            print('failed :(')
    

if __name__ == "__main__":
    main()