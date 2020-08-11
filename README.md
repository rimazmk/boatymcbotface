# boatymcbotface

On demand boat picures in your Slack workspace! Thanks UM Autonomy for the inspiration for this garbage. 

## Setup

Create venv and install dependencies

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Set environment variables

```bash
export ACCESS_TOKEN={your_slack_access_token}
export SIGNING_SECRET={your_slack_signing_secret}
export FLASK_APP=boatymcbotface
```

## Run

```bash
flask run
```
