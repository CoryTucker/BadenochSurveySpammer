import re
from openai import OpenAI

import data


# class which responds to a question given some info.
# this is the hard bit, hence why currently it's just a dummy class which returns the same thing each time.
# todo

class questionResponse:
    client: OpenAI
    api_key = ''

    def __init__(self):
        # attempt to grab the api_key from api_key.txt
        try:
            with open('api_key.txt', 'r') as file:
                self.api_key = file.readline()
        except FileNotFoundError:
            f = open('api_key.txt', 'x')
            self.api_key = ""

        if self.api_key:
            self.client = OpenAI(
                api_key=self.api_key,
            )
        else:
            self.client = fake_client

    def get_response(self, question_text):
        prompt = ''
        for i in data.questions:
            if re.search(i[0], question_text):
                prompt = i[1]
        if prompt:
            messages = [{"role": "system",
                         "content": prompt}]
            chat_completion = self.client.chat.completions.create(
                messages=messages
                ,
                model="gpt-3.5-turbo",
            )
            return chat_completion
        else:
            return 'bazinga'


# dummy class to allow testing without an openai API key
class fake_client:
    class chat:
        class completions:
            test = 0

            def __init(self):
                pass

            def create(messages, model):
                # python is being weird here but it doesn't matter because it's only a testing thing
                return 'wheeeee ' + messages[0]['content'][0:10]
