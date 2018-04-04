#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import threading
import goslate as GS
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re

class wxGameBot(WXBot):

    def __init__(self):
        WXBot.__init__(self)
        self.gs = GS.Goslate()

    def transform(self,text):
    	m = self.gs.translate(text,'en')
    	return self.gs.translate(m,'zh')
            
    def handle_msg_all(self, msg):
    	if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            if msg['content']['detail']['type'] == 'at' and msg['content']['detail']['value'] == 'Bot':
            	self.send_msg_by_uid(self.tranform(msg['content']['desc']),msg['user']['id'])
            
                    
def main():
    bot = wxGameBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()

if __name__ == '__main__':
    main()
