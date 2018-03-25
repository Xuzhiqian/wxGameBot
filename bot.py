#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re

class wxGameBot(WXBot):

    def __init__(self):
        WXBot.__init__(self)
            
    def handle_msg_all(self, msg):
            
                    
def main():
    bot = wxGameBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()

if __name__ == '__main__':
    main()
