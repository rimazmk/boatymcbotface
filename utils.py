import requests
import random
import os

URL = "https://www.reddit.com/r/boats.json"
SLACK_URL = "https://slack.com/api/chat.postMessage"
headers = { 'User-agent': 'Collegecow\'s bot' }
slack_access_token = os.environ['ACCESS_TOKEN']

def get_link():

    r = requests.get(URL, headers=headers)
    body = r.json()

    while True:

        post = random.choice(body['data']['children'])
        url = post['data']['url']

        if '.jpg' in url:
            return url

def send_message():
    print(slack_access_token)
    headers = {
        "Authorization": "Bearer " + slack_access_token,
        "Content-Type": "application/json"
    }
    data = {
        "channel": "bottesting",
        "text": "BOATS! " + get_link()
    }

    return requests.post(SLACK_URL, json=data, headers=headers)