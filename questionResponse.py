# from openai import OpenAI
# class which responds to a question given some info.
# this is the hard bit, hence why currently it's just a dummy class which returns the same thing each time.
# todo
class questionResponse:
    # client: OpenAI

    def __init__(self):
        # attempt to grab the api_key from api_key.txt
        try:
            with open('api_key.txt', 'r') as file:
                self.api_key = file.readline()
        except FileNotFoundError:
            f = open('api_key.txt', 'x')
            self.api_key = ""

    def get_response(self, questiontEXT):
        return 'bazinga'