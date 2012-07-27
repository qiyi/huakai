#!/usr/bin/env python
#coding:utf-8

import qmsg
import httpmethod

class Qreqmsg(qmsg.Qmsg):

    def __init__(self):
        qmsg.Qmsg.__init__(self)
        self.method = httpmethod.POST
        self.sendurl = None