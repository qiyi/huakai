#!/usr/bin/env python
#coding:utf-8

import qstatus

class Quser():

    def __init__(self, uin):
        self.uin = uin
        self.qnumber = "0"
        self.password = "0"
        self.clientid = -1
        self.name = None
        self.status = qstatus.offline

