import solver


def main():
    print('reordering word list')
    words = solver.get_words()
    words = [w for w in words if len(w) == 5]
    words = solver.rate_words(words=words)
    with open('valid_words.txt', 'w') as f:
        for i in range(len(words)):
            f.write(words[i])
            if(i < len(words)-1):
                f.write(' ')
        print('done')
        print('wrote {} words'.format(len(words)))


if __name__ == "__main__":
    main()
