import solver
import gzip
import pickle

def main():
    words = solver.get_words()
    print('creating dictionary')
    dict = {}
    for x in words:
        for y in words:
            dict[(x, y)] = solver.compare(x, y)

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