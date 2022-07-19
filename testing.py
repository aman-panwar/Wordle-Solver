from statistics import mean
from progress_bar import FixedUpdateProgressBar
import solver
from time import time


def main():
    test_words = solver.get_words()

    fails = []
    success_turn =[]

    try:
        progress_bar = FixedUpdateProgressBar("Testing words")
        progress_bar.start()
        start_time = time()
        for i in range(len(test_words)):
            test = test_words[i]
            words = solver.get_words()
            for turn in range(1, 8):
                if len(words) == 0 or turn == 7:
                    fails.append(test)
                    break

                guess = words[0]
                result = solver.compare(test, guess)
                if result == 'GGGGG':
                    success_turn.append(turn)
                    break
                words = solver.filter_words(
                    words=words, guess=guess, result=result)
                words = solver.rate_words(words)

            progress_bar.update((i+1)/len(test_words))
        timetaken = time() - start_time
        progress_bar.end()

        print('RESULT')
        print('avg guesses: {}'.format(round(mean(success_turn),2)))
        print('fail rate: {}%'.format(round(len(fails)/len(test_words)*100, 2)))
        print('avg time to result: {}'.format(round(timetaken/len(test_words), 2)))
        print('fails:')
        print(fails)
        print('')
    except:
        progress_bar.end()
        print('failed testing')


if __name__ == "__main__":
    main()
