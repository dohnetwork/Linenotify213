#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import requests,json
import urllib.parse
import pymysql
import urllib.request, urllib.error


#LINE_ACCESS_TOKEN="Q1KUFp76JYm7YPMzZAS9IlGKZhhlXx9gIuOIoJFLy48"
#url = "https://notify-api.line.me/api/notify"

conn = pymysql.connect(host='172.16.1.212', unix_socket='/tmp/mysql.sock', user='root', passwd='camel', db='phpmonitordb',charset='utf8')
cur = conn.cursor()
cur.execute("SELECT p1.label,p1.port,p2.message,p2.datetime,p2.line1,p1.ip,p2.log_id,p1.type FROM psm_servers AS p1 ,psm_log AS p2 where p1.server_id = p2.server_id AND  p2.line1 <> 1")
rows = cur.fetchall()
if len(rows) >0:
   for row in rows:
           if row[2].find("RUNNING") == -1 and row[7] == "website":
              url = row[5]
              print(row[5]+str(row[6]))
              try:
                connurl = urllib.request.urlopen(url)
              except urllib.error.HTTPError as e:
                # Return code error (e.g. 404, 501, ...)
                # ...
                print(e.code)
              except urllib.error.URLError as e:
                # Not an HTTP-specific error (e.g. connection refused)
                # ...
                print('URLError')
              else:
                # 200
                # ...
                print('good')
                cur.execute("UPDATE psm_log set line1 = 1 where psm_log.line1 <>1 and psm_log.log_id = "+str(row[6]))
                cur.execute("UPDATE  psm_servers set status = 'on' where  server_id = ",+str(row[6]))
               #message="เครื่อง "+row[0]+" SERVICE:"+str(row[1])+" ใช้งานได้แล้ว เวลา: "+str(row[3])
               #msg = urllib.parse.urlencode({"message":message})
               #LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
               #session = requests.Session()
               #a=session.post(url, headers=LINE_HEADERS, data=msg)
               #print(a.text)
           #else:
               #message="เครื่อง "+row[0]+" SERVICE:"+ str(row[1])+ " ล่ม เวลา: "+str(row[3])
               #msg = urllib.parse.urlencode({"message":message})
               #LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
               #session = requests.Session()
               #a=session.post(url, headers=LINE_HEADERS, data=msg)
               #print(a.text)
   #cur.execute("UPDATE psm_log set line1 = 1 where psm_log.line1 <>1")
cur.close()
conn.close()
