#!/usr/bin/env python
#coding:utf-8


import binascii
import hashlib

def qencry(password, token1, token2):
    password1 = md5hash(password)
    password2 = hex_md5hash(password1 + hexchar2bin(token2))
    password3 = hex_md5hash(password2 + token1.upper())
    return password3

'''from http://www.oschina.net/code/snippet_95475_11051'''
def md5hash(str):
    return hashlib.md5(str).digest()

def hex_md5hash(str):
    return hashlib.md5(str).hexdigest().upper()

def hexchar2bin(str):
    final_str = ""
    str = str.split('\\x')
    for i in str[1:]:
        final_str += chr(int(i, 16))

    return final_str

class Qalgorithm():

    def __init__(self):
        pass
