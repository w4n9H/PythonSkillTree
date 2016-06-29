# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/6/29
hail hydra!
"""

__author__ = "mango"
__version__ = "0.1"


import jwt
import time
import requests


AccessKey = "abc"
SecretKey = "1234567890"
payload = {
    'accesskey': AccessKey,
    'time': int(time.time())
}
headers = {
  "typ": "JWT",
  "alg": "HS256"
}
encoded = jwt.encode(payload, SecretKey)
url = "http://127.0.0.1:8080/v1/jwt_auth?jwt={jwt_code}".format(jwt_code=encoded)
r = requests.get(url)
print r.text



