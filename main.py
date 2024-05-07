import random
from fake_useragent import UserAgent
import time
import re
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import math
import data
from data import xPaths as xPaths
from questionResponse import questionResponse as questionResponse  # love this import
import concurrent.futures

erqwera
debugMode = False
randomWindowSize = False
# randomizes the window size. It's toggleable because it can be obnoxious.
enableThreading = False
maxThreads = 5
# not linked to cpu threads -
# this is more to do with how many browser windows your computer can cope with having open


def answer_survey():
    options = Options()
    if randomWindowSize:
        options.add_argument("window-size={0}".format(get_random_window_size()))
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    # individual randomisation for the survey

    # if the fake 'user' knows that they can tick multiple items in check boxes
    rand_num = random.random()
    if rand_num < 0.7345 or debugMode:
        picks_multiple_check_boxes = True
    else:
        picks_multiple_check_boxes = False

    # loops through all of the pages on the survey and dynamically grabs the questions.
    # uses the data (todo) to lookup what to do with a question name
    # picks random buttons on the radios
    while True:
        # get questions
        # check if it's a radiogroup (i.e. the selector questions
        questions = browser.find_elements(By.XPATH, xPaths['questions'])
        for question in questions:
            # look for radios. if we don't find any, move on to look for check boxes
            radio_items = question.find_elements(By.XPATH, xPaths['radio_items'])
            if radio_items:
                # if the radio items contain a 'please specify'
                # box where we're supposed to enter text, remove it, so we don't select it
                # (so far, it's not worth programming in any responses to these)
                if re.search(r'Other', radio_items[-1].text):
                    radio_items.pop(-1)
                # ugly 1 liner - selects a random item from the radio and clicks it
                radio_items[random.randrange(0, len(radio_items))].click()
                continue  # skip thr rest of the loop and continue to the next part
                # (won't try to parse the question in multiple ways)
                # only required because of my dumb code structure but ehhh it works

            # look for check_boxes. if we don't find any, move on to filling in the question string
            check_boxes = question.find_elements(By.XPATH, xPaths['checkbox_items'])
            if check_boxes:
                # like with radio items, remove the 'other' box
                if re.search(r'Other', check_boxes[-1].text):
                    check_boxes.pop(-1)
                # since we can select multiple items, this one is more interesting.
                # check for a 'don't know' item.
                if re.search(r"Don't know", check_boxes[-1].text):
                    if random.random() < 0.231415:  # Roll random to choose if the don't know is picked
                        check_boxes[-1].click()
                    else:
                        check_boxes.pop(-1)  # else, remove it, so it can't be picked as well as other multiple items

                # choose how many items we'll pick out of the remaining ones.
                # the math.pow makes the distribution non-linear (biased toward fewer items) for added randomness
                num_of_items = math.ceil(
                    math.pow(random.random(), 3) * len(check_boxes)
                )
                for i in range(num_of_items):  # click num_of_items random items in the check_boxes
                    # selects a random item from the check_box and clicks it
                    index = random.randrange(0, len(check_boxes))
                    check_boxes[index].click()
                    # then removes it so we can't pick it again
                    check_boxes.pop(index)

                continue  # skip thr rest of the loop and continue to the next question
            text_area = question.find_element(By.XPATH, xPaths['text_area'])
            text_area.send_keys(questionResponse.get_response(question.text))
        if debugMode:
            input()

        try:
            next_button = browser.find_element(By.XPATH, xPaths['next_page_button'])
        except selenium.common.exceptions.NoSuchElementException:
            # if we don't find a next button, then we've finished the survey and can instead press the finish button
            break
        # press the next button to move onto the next page of the survey
        next_button.click()
    if not debugMode:
        # actually press the submit button (currently disabled)
        # also disabled in debug mode
        submit = browser.find_element(By.XPATH, xPaths['submit_button'])
        # ## submit.click()
    else:
        input()
    global surveyCompletedCount
    surveyCompletedCount += 1
    global currentThreads
    currentThreads -= 1
    browser.quit()


def get_random_window_size():
    # really ugly way of selecting a random windows size based on percentages outlined in data
    num = random.random()
    for i in data.displayResolutions:
        if i[1] > num:
            return num
        else:
            num -= i[1]
    # if we still haven't found a suitable size, just pick something random
    return '{0},{1}'.format(random.randrange(562, 2134), random.randrange(850, 2687))


currentThreads = 0
surveyCompletedCount = 0
if __name__ == '__main__':
    print('e')
    url = data.url
    questionResponse = questionResponse()
    if not enableThreading:
        answer_survey()
    else:
        currentThreads = 0
        surveyCompletedCount = 0
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=maxThreads)
        counter = 0
        while True:
            if currentThreads < maxThreads:
                pool.submit(answer_survey)
                currentThreads += 1
            if counter < 20:
                counter += 1
            else:
                counter = 0
                print('surveysCompleted: {0}'.format(surveyCompletedCount))
            time.sleep(0.1)

