from API import Message, Keyboard, KeyboardButton
import json

with open("texts.json") as file:
    texts = json.load(file)

START_MESSAGE = Message(
    text=texts['start']
)
