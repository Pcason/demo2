# coding:utf-8
import sys
# import urllib
from urllib.parse import quote
import json
import time

s=json.dumps({"type":7,"objid":0,"page":4,"ajax":1,"retina":1})

aa=quote(s)
print(aa)
print(round(time.time()*1000))