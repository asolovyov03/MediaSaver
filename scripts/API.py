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
            keyboard.append(
                buttons[index:min(len(buttons) - 1, index + row_limit)])
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
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'sendMessage')
        body = {"chat_id": chat_id, "text": text}

        if parse_mode:
            body["parse_mode"] = parse_mode

        if keyboard:
            body.update(keyboard.get_json())

        return requests.post(url, json=body)

    @staticmethod
    def edit_message(
        chat_id: int,
        message_id: int,
        text: str,
        parse_mode: Optional[str] = None,
        keyboard: Optional[Keyboard] = None
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'editMessageText')
        body = {"chat_id": chat_id, "message_id": message_id, "text": text}

        if parse_mode:
            body["parse_mode"] = parse_mode

        if keyboard:
            body.update(keyboard.get_json())

        return requests.post(url, json=body)

    @staticmethod
    def send_photo(
        chat_id: int,
        file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'sendPhoto')
        body = {'chat_id': chat_id, 'photo': file_id}

        if caption:
            body['caption'] = caption

        if parse_mode:
            body['parse_mode'] = parse_mode

        return requests.post(url, json=body)

    @staticmethod
    def send_video(
        chat_id: int,
        file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'sendVideo')
        body = {'chat_id': chat_id, 'video': file_id}

        if caption:
            body['caption'] = caption

        if parse_mode:
            body['parse_mode'] = parse_mode

        return requests.post(url, json=body)

    @staticmethod
    def send_gif(
        chat_id: int,
        file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'sendAnimation')
        body = {'chat_id': chat_id, 'animation': file_id}

        if caption:
            body['caption'] = caption

        if parse_mode:
            body['parse_mode']

        return requests.post(url, json=body)

    @staticmethod
    def send_voice(
        chat_id: int,
        file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'sendVoice')
        body = {'chat_id': chat_id, 'file_id': file_id}

        if caption:
            body['caption'] = caption

        if parse_mode:
            body['parse_mode'] = parse_mode

        return requests.post(url, json=body)

    @staticmethod
    def send_video_note(
        chat_id: int,
        file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'sendVideoNote')
        body = {'chat_id': chat_id, 'video_note': file_id}

        if caption:
            body['caption'] = caption

        if parse_mode:
            body['parse_mode'] = parse_mode

        return requests.post(url, json=body)

    @staticmethod
    def send_document(
        chat_id: int,
        file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None
    ) -> requests.models.Response:
        url = telegram['url'].format(telegram['token'], 'sendDocument')
        body = {'chat_id': chat_id, 'document': file_id}

        if caption:
            body['caption'] = caption

        if parse_mode:
            body['parse_mode'] = parse_mode

        return requests.post(url, json=body)
