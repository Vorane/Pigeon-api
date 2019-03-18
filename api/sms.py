import importlib
import os
import africastalking

try:
    dotenv = importlib.import_module('dotenv')
    dotenv.load_dotenv(dotenv.find_dotenv())
except ModuleNotFoundError:
    pass

username = os.environ.get('SMS_USERNAME')
api_key = os.environ.get('SMS_API_KEY')

africastalking.initialize(username, api_key)
sms = africastalking.SMS


def finish_callback(error, response):
    if error is not None:
        raise error
    print(response)


def send_sms(message, recepient):
    sms.send(message, [recepient], callback=finish_callback)

send_sms("Hi Paul","+254716544925")
