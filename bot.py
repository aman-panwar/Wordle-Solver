import sys
from time import sleep
from unittest import result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import solver


words = solver.get_words()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options =chrome_options)
browser.get('https://www.nytimes.com/games/wordle/index.html')

def get_guess():
    if len(words) == 0: 
        raise Exception('No valid guesses :(')
    return words[0]
def get_result(turn):
    try:
        result = ""
        tile_to_str = {
            "correct": 'G',
            "present": 'Y',
            "absent": 'W'
        }
        for col in range(1,6):
            tile  = browser.find_element(By.XPATH, '//*[@id="wordle-app-game"]/div[1]/div/div[{row}]/div[{col}]/div'.format(row = turn,col = col))
            result = result + tile_to_str[tile.get_attribute('data-state')]
        return result
    except: raise Exception('Could not recieve result from the game. Try running again or use solver.py instead.')
def enter_guess(word):
    try:
        for chr in word:
            key= browser.find_element(By.XPATH, '//*[@id="wordle-app-game"]/div[2]/*/button[@data-key=\'{}\']'.format(chr))
            key.click()
            sleep(0.1)
        browser.find_element(By.XPATH, '//*[@id="wordle-app-game"]/div[2]/div[3]/button[1]').click()
        sleep(2)
    except: raise Exception('Problem occured in submitting guess. \nPossible cause: the browser window was not in focus.\nTry running the script again.')
def init_start_of_game():
    try:
        browser.find_element(By.XPATH, '/html/body/div/div/dialog/div/button').click()
        sleep(1)
    except: raise Exception('Script did not recognise the website UI. Try using solver.py')

try:
    init_start_of_game()
    for turn in range(1,7):
        guess = get_guess()
        enter_guess(guess)
        result = get_result(turn)
        if result == 'GGGGG': break
        words = solver.filter_words(words=words, guess=guess,result=result)
        words = solver.rate_words(words)
        

except Exception as err:
    print("Error Occured\n", err)