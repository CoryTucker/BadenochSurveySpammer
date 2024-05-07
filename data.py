# survey url (it just felt wrong to put this in main.py while this file exists)
url = 'https://www.smartsurvey.co.uk/s/55NP2K/'

# contains the xPaths to each element we need to grab whilst completing the survey.
# I could hardcode this, but it's a lot easier to give them names here because it makes changing stuff a lot simpler.

# if something is broken, take a look at this: https://devhints.io/xpath, which roughly explains how xPaths work.
# figure out how to access the elements by inspecting the page or something

# it's not really the type of structure you're supposed to use (it should be in a file or something) but i don't care
xPaths = {
    'next_page_button': "//div[@class='ss-survey-button-holder']//input[@value='Next Page']",
    'submit_button': "//div[@class='ss-survey-button-holder']//input[@value='Finish Survey']",
    'questions': "//div[contains(@class, 'ss-survey-inner-body')]/div[contains(@class,'ss-question-holder-top')]",
    'radio_items': "*//div[@role='radiogroup']//ul/li",
    'checkbox_items': "*//div[contains(@aria-labelledby, 'checkboxgroup')]//ul/li",
    'text_area': "*//*[contains(@class, 'ss-input-text') or contains(@class, 'ss-input-textarea')]",

}

# todo
# contains regex expressions which match one of each of the 4 questions we need to generate a response for.
# the matched question is paired with a gpt prompt which i haven't made yet.
questions = {
    r'*Please attach your example*': '',
    r'*What issues about how single-sex services or spaces operate*': '',
    r'*What is the name*produced this policy*': '',
    r'*what is/are the name/s*use this policy*': '',
}

displayResolutions = [
    ('1366,768', .22),
    ('1920,1080', .20),
    ('1536,864', .085),
    ('1440,900', .07),
    ('1280,720', .048),
    ('1600,900', .041),
    ('1280,800', .029),
    ('1280,1024', .026),
    ('1024,768', .025),
    ('768,1024', .024),
]
