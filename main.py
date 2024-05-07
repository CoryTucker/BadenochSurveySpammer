import random
import time
import re
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import data
from data import xPaths as xPaths
from questionResponse import questionResponse as questionResponse  # love this import

url = data.url
questionResponse = questionResponse()
debugMode = True


def answer_survey():
    browser = webdriver.Chrome()
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
                    math.pow(random.random(), 3)*len(check_boxes)
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


if __name__ == '__main__':
    answer_survey()
    if debugMode:
        input()
