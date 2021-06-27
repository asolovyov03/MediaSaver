"""
    Scripts for working with Telegram Bot API    
"""

from typing import Optional, Dict, List
from config import telegram
import requests
import random


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


class InlineQueryResult:
    """
        Class representing Telegram InlineQueryResult

        Attributes:
            media_type: A kind of the media. Can be one of these:
                - photo
                - gif
                - mpeg4_gif
                - video
                - audio
                - voice
                - document
            url: A valid address of the file
            title: A title of the result
            Caption: Optional; A caption of the resuult if required
            Parse_mode: Optional; A mode for parsing text (can be HTML and Markdown)
    """

    def __init__(self, media_type: str, url: str, title: str,
                 caption: Optional[str] = None, parse_mode: Optional[str] = None) -> None:
        self.type = media_type
        self.id = str(random.getrandbits(64))
        self.url = url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode

    def get_json(self) -> Dict[str, str]:
        data = {'type': self.type, 'id': self.id, 'title': self.title}
        if self.type == 'photo':
            data['photo_url'] = self.url
        elif self.type == 'gif':
            data['gif_url'] = self.url
        elif self.type == 'mpeg4_gif':
            data['mpeg4_url'] = self.url
        elif self.type == 'video':
            data['video_url'] = self.url
        elif self.type == 'audio':
            data['audio_url'] = self.url
        elif self.type == 'voice':
            data['voice_url'] = self.url
        elif self.type == 'document':
            data['document_url'] = self.url

        if self.caption:
            data['caption'] = self.caption

        if self.parse_mode:
            data['parse_mode'] = self.parse_mode

        return data


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
