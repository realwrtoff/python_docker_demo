#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define('port', default=8080, help='run on the given port', type=int)


class Request(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        status = 200
        try:
            name = self.get_argument('name')
            age = self.get_argument('age')
            dic = {'name': name, 'age': int(age)}
        except Exception as e:
            status = 501
            dic = {'msg': '{0}'.format(e)}
        dic['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        msg = json.dumps(dic)
        self.set_status(status)
        self.write(msg)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/request', Request)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
