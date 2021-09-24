#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import requests,json
#import urllib.parse
#import pymysql
LINE_ACCESS_TOKEN="i5LlpTX9n0zq62zk5sq1K1qSzQYouZJIT2U6flbnDIl"
#LINE_ACCESS_TOKEN="Q1KUFp76JYm7YPMzZAS9IlGKZhhlXx9gIuOIoJFLy48"
url = "https://notify-api.line.me/api/notify"
message="อิศเรศ สุวัฒน์พิศาลกิจ"
msg = urllib.parse.urlencode({"message":message})
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
a=session.post(url, headers=LINE_HEADERS, data=msg)
print(a.text)
