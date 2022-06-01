# Wordle Solver

The goals was to create a bot solver which automatically solves the wordle for you. This program solves the wordle with succes rate of 99.48% and takes 3.55 tries on average.

'bot.py' is the bot that automatically solves the wordle for you. It uses Selenium and pynput to automate the solving for you. Run the script and that should do the work for you.

'solver.py' contains the logic for solving wordle. In case 'bot.py' fails, 'solver.py' can be used to manually take input and generate a guess. 
'solver.py' takes input as 5 letter string formed only by 'G', 'Y', 'W'.
'G' (green) represents present and in right place
'Y' (yellow) represents present but in wrong place
'W' (grey/white) represents not present

'valid_words.txt' contains all the valid wordle guesses

'recreate_dict.py' should be run incase changes are made to 'valid_words.txt'. The program pre process the words and saves the result in 'dictionary.pkl' 