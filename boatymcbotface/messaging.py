from slackeventsapi import SlackEventAdapter
import os
from emoji import emojize
from . import app
from .utils import send_message, send_picture

INTRO_MESSAGE = '''
    Boats. You need em, I got em. What else needs to be said? 
    Check out my code here :point_right: :sunglasses: :point_right: 
    https://github.com/rimazk123/boatymcbotface
    '''
SIGNING_SECRET = os.environ['SIGNING_SECRET']
slack_events_adapter = SlackEventAdapter(SIGNING_SECRET, "/slack/events", app)


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    msg = event_data['event']['text']
    channel = event_data['event']['channel']

    if 'introduce yourself' in msg:
        send_message(emojize(INTRO_MESSAGE), channel)
    else:
        send_message('BOATS!!', channel)
        send_picture(event_data['event']['channel'])
