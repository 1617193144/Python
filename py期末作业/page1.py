#-*- coding:utf-8 –*-
import urllib
import urllib2
import re
import thread
import time

class caihaopage1:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'
        self.pageStories = []
        self.url = 'http://qiqihaer.baixing.com/search/?page=1'
        self.headers = {'User-Agent': self.user_agent}

    def getpage(self, index):
        user_agant = self.user_agent
        url = self.url
        headers = {'User-Agent': user_agant}
        result = urllib2.Request( url, headers=headers )
        response = urllib2.urlopen( result )
        pageCode = response.read().decode( 'utf-8' )
        return pageCode

    def pageindex(self, index):
        pageCode = self.getpage( index )
        pattern = re.compile('<div class.*?>.*?<span class=.*?>.*?<a href=.*?>(.*?)</a>.*?<div class.*?>(.*?)</div>.*?<div class.*?>(.*?)</div>',re.S)
        items = re.findall( pattern, pageCode )
        for i in items:
            for g in i:
                input = raw_input()
                print g

    def start(self):
        print "--------------------------------------page1------------------------------------"
        print "-------------             i'm    Separation   line         --------------------"
        self.getpage(index=caihaopage1)
        self.pageindex(index=caihaopage1)

