from flask import Flask

app = Flask(__name__)

import boatymcbotface.messaging
import boatymcbotface.utils
import boatymcbotface.scheduler
