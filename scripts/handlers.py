from typing import Dict, Any
from API import API
from templates import START_MESSAGE


class CommandHandler:
    '''
        Class for responding on commands
    '''

    def __init__(self, message: Dict[str, Any]) -> None:
        # get the whole message text including the command
        self.command = message['text']
        self.user = message['from']
        self.chat_id = message['chat']
        self.execute()

    def execute(self):
        '''
            Make some actions according to the command
        '''

        if '/start' in self.command:
            API.send_message(
                chat_id=self.chat_id,
                message=START_MESSAGE
            )
