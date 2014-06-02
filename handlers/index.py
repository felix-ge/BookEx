#coding:utf-8

import tornado.web
from model.entity import Entity

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        entity = Entity('the5fire\'s blog')
        self.render('index.html', entity = entity)


