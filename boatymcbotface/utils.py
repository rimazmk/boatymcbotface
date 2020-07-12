import requests
import random
import os

BOATS_URL = "https://www.reddit.com/r/boats.json"
SLACK_URL = "https://slack.com/api/chat.postMessage"
headers = {'User-agent': 'rimaz\'s bot'}
slack_access_token = os.environ['ACCESS_TOKEN']


def get_link():
    r = requests.get(BOATS_URL, headers=headers)
    body = r.json()

    while True:

        post = random.choice(body['data']['children'])
        url = post['data']['url']

        if '.jpg' in url:
            return url


def send_message(message, channel):
    headers = {
        "Authorization": "Bearer " + slack_access_token,
        "Content-Type": "application/json"
    }
    data = {
        "channel": channel,
        "text": message
    }

    return requests.post(SLACK_URL, json=data, headers=headers)


def send_picture(channel):
    return send_message(get_link(), channel)
