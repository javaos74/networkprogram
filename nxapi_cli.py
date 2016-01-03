#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

url='http://10.72.86.51/ins'
switchuser='admin'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version ; show interface brief ;xxxx ;",
      "version": 1
    },
    "id": 1
  }]
response = requests.post(url,data=json.dumps(payload), 
headers=myheaders,auth=(switchuser,switchpassword)).json()
print  str(response)
