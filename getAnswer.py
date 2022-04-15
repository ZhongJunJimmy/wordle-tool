from selenium import webdriver
import json

wd = webdriver.Chrome('./chromedriver')
wd.get("https://www.nytimes.com/games/wordle/index.html")
strWordleLocalStorage = wd.execute_script("return window.localStorage.getItem('nyt-wordle-state')")
wordleState = json.loads(strWordleLocalStorage)
print('The answer of today\'s wordle: ' + wordleState['solution'])
wd.close()
