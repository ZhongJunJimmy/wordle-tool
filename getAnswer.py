from selenium import webdriver
import json
import datetime

# get the wordle solution from local storage
def getSolutionFromLocalStorage():
    # set chromedriver path
    chromePath = './chromedriver'

    # set chromedriver option that does not open the browser
    option = webdriver.ChromeOptions()
    option.add_argument("headless")

    # start chrome driver and access web by URL
    wd = webdriver.Chrome(chromePath, chrome_options=option)
    wd.get("https://www.nytimes.com/games/wordle/index.html")

    # run command to get the local storage contents
    strWordleLocalStorage = wd.execute_script("return window.localStorage.getItem('nyt-wordle-state')")

    # conver local storage string to json format
    wordleState = json.loads(strWordleLocalStorage)
    wd.close()

    return wordleState['solution']


def recordAnswer(solution):
    f = open("solution.txt", "a")
    f.writelines("["+ str(datetime.datetime.now()) +"]" + solution + "\n")
    f.close()
    return 1

if __name__ == "__main__":
    wordleSolution = getSolutionFromLocalStorage()
    print("["+ str(datetime.datetime.now()) +"]" +  wordleSolution)
    result = recordAnswer(wordleSolution)
    