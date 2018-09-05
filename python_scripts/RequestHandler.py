#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ben liu"

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json
import urlparse
import wx_refund
from SocketServer import ThreadingMixIn

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        response = {
            'status':'SUCCESS',
            'data':'call success!'
        }
        parsed_path = urlparse.urlparse(self.path)
        query = parsed_path.query
        print query
        dict = {}
        list = query.split('&')
        print list
        for item in list:
            temp = item.split('=')
            tempDict = {temp[0]:temp[1]}
            dict.update(tempDict)
        # 调用退款接口返回数据
        xml = wx_refund.requestWx(dict) 
        print xml
        # if xml is not None :
        #     wx_refund.getResult(xml)
        self._set_headers()
        self.wfile.write(json.dumps(response))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print 'post data from client:'
        print post_data

        response = {
            'status':'SUCCESS',
            'data':'server got your post data'
        }
        self._set_headers()
        self.wfile.write(json.dumps(response))
# 创建支持多进程的http server,只需要继承forkingMixIn类
class ThreadHttpServer(ThreadingMixIn,HTTPServer):
    pass
if __name__ == '__main__':
    port = 80
    server = ThreadHttpServer(('', port), RequestHandler)
    print('Listening on localhost:%s' % port)
    server.serve_forever()