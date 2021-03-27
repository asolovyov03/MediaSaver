"""
    Scripts for working with Telegram Bot API    
"""

from typing import Optional, Dict, List
from config import telegram
import requests


class KeyboardButton:
    """
        Class representing InlineKeyboardButton
    """
    def __init__(self, text: str, callback_data: str) -> None:
        self.text = text,
        self.callback_data = callback_data

    def get_json(self) -> Dict[str, str]:
        """
            Function returning dictionary for parsing
        """
        return {"text": self.text, "callback_data": self.callback_data}


class Keyboard:
    """
        Class representing Telegram InlineKeyboardMarkup
    """
    def __init__(self, buttons: List[KeyboardButton], row_limit: int = 10) -> None:
        keyboard = []
        for index in range(0, len(buttons), row_limit):
            keyboard.append(buttons[index:min(len(buttons) - 1, index + row_limit)])
        self.keyboard = keyboard

    def get_json(self) -> Dict[str, list]:
        """
            Function returning dictionary for parsing
        """
        return {"inline_keyboard": self.keyboard}


class API:
    """
        Class for working with Telegram API methods
    """

    @staticmethod
    def send_message(
        chat_id: int,
        text: str,
        parse_mode: Optional[str] = None,
        keyboard: Optional[Keyboard] = None
    ) -> None:
        url = telegram['url'].format(telegram['token'], 'send_message')
        body = {"chat_id": chat_id, "text": text}

        if parse_mode:
            body["parse_mode"] = parse_mode

        if keyboard:
            body.update(keyboard.get_json())

        requests.post(url, json=body)

    @staticmethod
    def edit_message(
        chat_id: int,
        message_id: int,
        text: str,
        parse_mode: Optional[str] = None,
        keyboard: Optional[Keyboard] = None
    ) -> None:
        url = telegram['url'].format(telegram['token'], 'edit_message')
        body = {"chat_id": chat_id, "message_id": message_id, "text": text}

        if parse_mode:
            body["parse_mode"] = parse_mode

        if keyboard:
            body.update(keyboard.get_json())

        requests.post(url, json=body)
