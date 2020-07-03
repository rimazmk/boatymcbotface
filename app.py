from flask import Flask, Response
from utils import send_message
from slackeventsapi import SlackEventAdapter
from slack import WebClient
import os
from threading import Thread

app = Flask(__name__)
SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
slack_events_adapter = SlackEventAdapter(SIGNING_SECRET, "/slack/events", app)

@app.route('/', methods=['GET'])
def hello():
    r = send_message('bottesting').json()
    print(r)
    return "message sent"


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    send_message(event_data['event']['channel'])

if __name__ == '__main__':
    app.run()
