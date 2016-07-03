#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-06-22 16:53:07
# Project: bili1

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.bilibili.com/index/rank/rookie-30-4.json', callback=self.index_page)

    def index_page (self, response):
        avlist=[]
        for x in response.json['rank']['list']:
            avlist.append(x['aid'])
            for aid in avlist:
                self.crawl('http://www.bilibili.com/video/av'+ str(aid), callback=self.detail_page)




   # @config(age=10 * 24 * 60 * 60)
  #  def index_page(self, response):
  #      for each in response.doc('a[href^="http"]').items():
  #          self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
           "time": response.doc('[itemprop="startDate"] i').text(),
       }
