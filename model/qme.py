#!/usr/bin/env python
#coding:utf-8

import quser
import qsession
import requests
import httpmethod
import qloginreq
import qloginrsp

class Qme(quser.Quser):
    
    def __init__(self, qnumber, password):
        quser.Quser.__init__(self, qnumber)
        self.qnumber = qnumber
        self.password = password
        self.session = requests.session()
        self.qsession = qsession.Qsession()

    def login(self, status):
        loginreq = qloginreq.Qloginreq(self.qsession, status)
        response = self.sendmsg(loginreq)
        loginrsp = qloginrsp.Qloginrsp(response.text)
        return loginrsp

    def sendmsg(self, msg):
        #print("send {content} to {url} ...".format(**{"content": msg.content, "url":msg.sendurl}))
        headers = {"Referer": "http://web.qq.com"}
        if msg.method == httpmethod.POST:
            response  = self.session.post(msg.sendurl, data=msg.content, headers=headers)
        else:
            response = self.session.get(msg.sendurl, params=msg.content, headers=headers)
        if not response.ok:
            raise Exception("Send msg {msg} failed".format(
                **{"msg": msg.toString()}))
        return response