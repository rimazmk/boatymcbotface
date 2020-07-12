from slackeventsapi import SlackEventAdapter
import os
from . import app
from .utils import send_message


SIGNING_SECRET = os.environ['SIGNING_SECRET']
slack_events_adapter = SlackEventAdapter(SIGNING_SECRET, "/slack/events", app)


@app.route('/', methods=['GET'])
def hello():
    r = send_message('bottesting').json()
    print(r)
    return "message sent"


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    send_message(event_data['event']['channel'])
