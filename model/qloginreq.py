#!/usr/bin/env python
#coding:utf-8

import qreqmsg
import httpmethod
import json

class Qloginreq(qreqmsg.Qreqmsg):

    def __init__(self, qsession, status):
        qreqmsg.Qreqmsg.__init__(self)
        self.sendurl = "http://d.web2.qq.com/channel/login2"
        self.method = httpmethod.POST
        self.status = status
        self.content = {
            "r": json.dumps({
                "status": status,
                "ptwebqq": qsession.ptwebqq,
                "passwd_sig": "",
                "clientid": qsession.clientid,
                "psessionid": None}), 
            "clientid": qsession.clientid,
            "psessionid": "null"}
