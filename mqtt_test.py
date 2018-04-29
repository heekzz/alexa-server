import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import urllib.request
import paho.mqtt.client as mqtt

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    welcome_msg = render_template('welcome_mqtt')

    return question(welcome_msg)


@ask.intent("MqttIntent")
def say_message(message):
    print(message)

    if message == 'hello':
        answer = 'Fuck yeah'
    else:
        answer = 'Fail'

    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.publish("/hakansson/test", "testing")
    return statement(answer)


# @ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
# def answer(first, second, third):
#     winning_numbers = session.attributes['numbers']
#
#     if [first, second, third] == winning_numbers:
#
#         msg = render_template('win')
#
#     else:
#
#         msg = render_template('lose')
#
#     return statement(msg)
#

if __name__ == '__main__':
    app.run(debug=True)
