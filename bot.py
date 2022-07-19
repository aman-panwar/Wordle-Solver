from time import sleep
from unittest import result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import solver


words = solver.get_words()

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://www.nytimes.com/games/wordle/index.html')

def get_guess():
    if len(words) == 0:
        raise Exception('No valid guess')
    return words[0]


def get_result(turn):
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


def enter_guess(word):
    keyboard = Controller()
    for c in word:
        keyboard.press(c)
        keyboard.release(c)
        sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)



browser.find_element(By.XPATH, '//*[@id="wordle-app-game"]/div[3]/div/div').click()
sleep(1)
for turn in range(1,7):
    guess = get_guess()
    enter_guess(guess)
    result = get_result(turn)
    if result == 'GGGGG':
        break
    words = solver.filter_words(words=words, guess=guess,
                                result=result)
    words = solver.rate_words(words)
