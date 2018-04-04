#!/usr/bin/env python
# coding: utf-8

import goslate as GS
import sys
import threading
from wxbot import *
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')
import re


class wxGameBot(WXBot):

    def __init__(self):
        WXBot.__init__(self)
        proxy_handler = urllib2.ProxyHandler({"http" : "http://proxy-domain.name:8080"})
        proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
                                    urllib2.HTTPSHandler(proxy_handler))
        self.gs = GS.Goslate(opener=proxy_opener)
        
    def transform(self, text):
        m = self.gs.translate(text, 'en')
        return self.gs.translate(m, 'zh')

    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            if msg['content']['detail'][0]['type'] == 'at' and msg['content']['detail'][0]['value'] == u'Bot':
                self.send_msg_by_uid(self.transform(msg['content']['desc']), msg['user']['id'])


def main():
    bot = wxGameBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()


if __name__ == '__main__':
    main()
