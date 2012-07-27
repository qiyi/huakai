#!/usr/bin/env python
#coding:utf-8

class Qsession():

    def __init__(self):
        self.ptvfsession = None
        self.ptcz = None
        self.skey = None
        self.ptwebqq = None
        self.uin = 0
        self.ptisp = None
        self.pt2gguin = None
        self.psessionid = None
        self.vfwebqq = None
        self.clientid = None

    def toString(self):
        sessionstring = "ptvfsession={ptvfsession}".format(**{"ptvfsession": self.ptvfsession})
        sessionstring += ", ptcz={ptcz}".format(**{"ptcz": self.ptcz})
        sessionstring += ", skey={skey}".format(**{"skey": self.skey})
        sessionstring += ", ptwebqq={ptwebqq}".format(**{"ptwebqq": self.ptwebqq})
        sessionstring += ", uin={uin}".format(**{"uin": self.uin})
        sessionstring += ", ptisp={ptisp}".format(**{"ptisp": self.ptisp})
        sessionstring += ", pt2gguin={pt2gguin}".format(**{"pt2gguin": self.pt2gguin})
        sessionstring += ", psessionid={psessionid}".format(**{"psessionid": self.psessionid})
        sessionstring += ", vfwebqq={vfwebqq}".format(**{"vfwebqq": self.vfwebqq})
        sessionstring += ", clientid={clientid}".format(**{"clientid": self.clientid})
        return sessionstring