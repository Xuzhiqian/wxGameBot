#!/usr/bin/env python
# coding: utf-8

import httplib
import md5
import random
import sys
import threading
import urllib
from wxbot import *

reload(sys)
sys.setdefaultencoding('utf-8')
import re


class Tran:
    def __init__(self):
        self.appid = '20180404000142953'
        self.secretKey = 'Ti2kr9gXh6xvY0yG1F4c'
        self.httpClient = None
        self.myurl = '/api/trans/vip/translate'
        self.salt = random.randint(32768, 65536)

    def translate(self, text, targetLang):
        self.sign = self.appid + text + str(self.salt) + self.secretKey
        m1 = md5.new()
        m1.update(self.sign)
        self.sign = m1.hexdigest()
        self.myurl = self.myurl + '?appid=' + self.appid + '&q=' + urllib.quote(
            text.encode('utf-8')) + '&from=auto' + '&to=' + targetLang + '&salt=' + str(self.salt) + '&sign=' + self.sign

        result = ''
        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            print response.read()
            print response
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()

    def transform(self, text):
        return ''


class wxGameBot(WXBot):

    def __init__(self):
        WXBot.__init__(self)
        self.T = Tran()

    def transform(self, text):
        return ''

    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            if msg['content']['detail'][0]['type'] == 'at' and msg['content']['detail'][0]['value'] == u'Bot':
                self.T.translate(msg['content']['desc'], 'en')
                # self.send_msg_by_uid(self.transform(msg['content']['desc']), msg['user']['id'])


def main():
    bot = wxGameBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()


if __name__ == '__main__':
    main()
