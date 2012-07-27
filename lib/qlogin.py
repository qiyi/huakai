#!/usr/bin/env python
#coding:utf-8

import sys, os

if not __file__ in sys.path:
    curdir = os.path.dirname(os.path.abspath(__file__))
    updir = os.path.dirname(curdir)
    sys.path.append(updir)

import model.qme as qme
import qalgorithm
import random
import requests
import model.qstatus as qstatus
import model.qloginreq as qloginreq

class Qlogin():

    def __init__(self, uin, password):
        self.me = qme.Qme(uin, password)

    def login(self):
        checkurl = "http://check.ptlogin2.qq.com/check?uin={uin}&appid=1003903&r={random}".format(
            **{"uin":self.me.uin, "random":str(random.random())})
        response = self.me.session.get(checkurl)
        if not response.ok:
            raise Exception("connect to {checkurl} failed.".format(
                **{"checkurl":checkurl}))

        tokens = self.parseCheckResult(response.text)
        
        encryedpass = qalgorithm.qencry(self.me.password, tokens[0], tokens[1])

        loginurl = "http://ptlogin2.qq.com/login?u={uin}&p={pass}".format(
            **{"uin": self.me.uin, "pass": encryedpass})
        loginurl += "&verifycode={token1}&webqq_type=10&remember_uin=1".format(
            **{"token1":tokens[0]})
        loginurl += "&login2qq=0&aid=1003903&u1=http%3A%2F%2Fweb.qq.com%2Floginproxy.html%3Flogin2qq%3D0%26webqq_type%3D10"
        loginurl += "&h=1&ptredirect=0&ptlang=2052&from_ui=1&pttype=1&dumy="
        loginurl += "&fp=loginerroralert&action=40-111-1157668&mibao_css=m_webqq&t=1&g=1" 

        response = self.me.session.get(loginurl)
        if not response.ok:
            raise Exception("login failed.")

        self.me.qsession.ptvfsession = response.cookies.get("ptvfsession")
        self.me.qsession.ptcz = response.cookies.get("ptcz")
        self.me.qsession.pt2gguin = response.cookies.get("pt2gguin")
        self.me.qsession.ptisp = response.cookies.get("ptisp")
        self.me.qsession.ptwebqq = response.cookies.get("ptwebqq")
        self.me.qsession.skey = response.cookies.get("skey")
        self.me.qsession.uin = response.cookies.get("uin")
        self.me.qsession.clientid = self.genclientid()

        loginrsp = self.me.login(qstatus.online)
        self.me.qsession.psessionid = loginrsp.psessionid
        self.me.qsession.vfwebqq = loginrsp.vfwebqq
        self.me.qsession.uin = loginrsp.uin
        self.me.status = loginrsp.status

        print("login succeed.")
        print(self.me.qsession.toString())
        return self.me

    def parseCheckResult(self, result):
        firstsp = result.rsplit("'")
        if firstsp[1] != "0":
            raise Exception("need vcode image")
        return [firstsp[3], firstsp[5]]

    def parseLoginResule(self, result):
        firstsp = result.rsplit("'")
        if firstsp[1] != "0":
            raise Exception("login failed")
        return 

    def genclientid(self):
        return "19860125"

if __name__ == '__main__':
    qqlogin = Qlogin("528711130", "1234567890")
    me = qqlogin.login()


