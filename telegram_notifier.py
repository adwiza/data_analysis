# encoding: utf-8

import telegram
from yaml import load
import os

class Notifier:
    
    def __init__(self, username):
        self.username = username        
        self.messages_counter = 0
        
        self.config = load( open( os.path.join(os.path.dirname( os.path.abspath(__file__) ), 'config.yaml'), 'r' ) )
        
        self.bot = telegram.Bot( self.config['bot_token'] )
    
    def counterUp(self):
        self.messages_counter += 1
    
    def notification(self, message):
        
        if self.username in self.config['users']:
            self.bot.sendMessage(chat_id = self.config['users'][self.username], text = message)
        
        else:
            print('Имя пользователя не найдено в файле config.yaml')