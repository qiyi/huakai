#!/usr/bin/env python
#coding:utf-8

class Qmsg():

    def __init__(self):
        self.uin = "0";
        self.number = "0";
        self.name = "";
        self.content = None

    def toString(self):
        contentstring = "uin={uin}".format(**{"uin": self.uin})
        return contentstring