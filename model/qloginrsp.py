#!/usr/bin/env python
#coding:utf-8

import qrspmsg
import json

class Qloginrsp(qrspmsg.Qrspmsg):
    
    def __init__(self, content):
        decontent = json.loads(content)["result"]
        self.uin = decontent["uin"]
        self.status = decontent["status"]
        self.psessionid = decontent["psessionid"]
        self.vfwebqq = decontent["vfwebqq"]