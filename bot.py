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

game = browser.find_element(By.TAG_NAME, 'game-app')
board = browser.execute_script(
    "return arguments[0].shadowRoot.getElementById('board')", game)
rows = board.find_elements(By.TAG_NAME, 'game-row')


def get_guess():
    if len(words) == 0:
        raise Exception('No valid guess')
    return words[0]


def get_result():
    result = ""
    row = browser.execute_script(
        'return arguments[0].shadowRoot', rows[turn])
    tiles = row.find_elements(By.CSS_SELECTOR, "game-tile")
    evalutation = {
        "correct": 'G',
        "present": 'Y',
        "absent": 'W'
    }
    for tile in tiles:
        result = result + evalutation[tile.get_attribute("evaluation")]
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



browser.find_element(By.XPATH, '//html').click()
sleep(1)
for turn in range(6):
    guess = get_guess()
    enter_guess(guess)
    result = get_result()
    if result == 'GGGGG':
        break
    words = solver.filter_words(words=words, guess=guess,
                                result=result)
    words = solver.rate_words(words)
