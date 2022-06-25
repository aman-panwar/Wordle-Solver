import solver
import gzip
import pickle


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

def main():
    words = solver.get_words()
    print('creating dictionary')
    dict = {}
    for x in words:
        for y in words:
            dict[(x, y)] = compare(x, y)

    print('saving dictionary')
    with gzip.open('dictionary.pklz', 'wb') as f:
        pickle.dump(dict, f)

    words = solver.rate_words(words=words, dict=dict)
    with open('valid_words.txt', 'w') as f:
        for i in range(len(words)):
            f.write(words[i])
            if(i<len(words)-1):
                f.write(' ')

    print('done')

if __name__ == "__main__":
    main()