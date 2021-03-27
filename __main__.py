'''
    Script launch the bot
'''

from flask import Flask
from flask import request
from scripts.config import telegram

app = Flask(__name__)

@app.route(f"/{telegram['token']}", methods = ['GET', 'POST'])
def get_updates():
    '''
        Get updates on bot
    '''

    if request.method == "POST":
        updates = request.get_json()
