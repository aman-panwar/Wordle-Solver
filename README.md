# Wordle Solver

The goals was to create a bot solver which automatically solves the wordle for you. This program solves the wordle with succes rate of 99.48% and takes 3.55 tries on average.

'bot.py' is the bot that automatically solves the wordle for you. It uses Selenium and pynput to automate the solving for you. Run the script and that should do the work for you.

'solver.py' contains the logic for solving wordle. In case 'bot.py' fails, 'solver.py' can be used to manually get input/output. This will be useful if the wordle's html is changed in future, in which case the bot might not work.
'solver.py' takes input as 5 letter string formed only by 'G', 'Y', 'W'.\
'G' (green) represents present and in right place\
'Y' (yellow) represents present but in wrong place\
'W' (grey/white) represents not present

'valid_words.txt' contains all the valid wordle guesses

'pre_process.py' should be run incase changes are made to 'valid_words.txt'. The program reorders the words in 'valid_words.txt' for optimal working of the program.