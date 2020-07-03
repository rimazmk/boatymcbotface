from flask import Flask, Response
from utils import send_message
from slackeventsapi import SlackEventAdapter
from slack import WebClient
import os
from threading import Thread

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    r = send_message().json()
    print(r)
    return "message sent"

if __name__ == '__main__':
    app.run()
    