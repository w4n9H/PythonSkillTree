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
import functools
import inspect
import base64
import json
import redis


auth_redis = {
    'host': '192.168.13.193',
    'port': 6379,
    'db': 1
}


def get_key(access_key):
    r = redis.Redis(host=auth_redis['host'], port=auth_redis['port'], db=auth_redis['db'])
    return r.mget(access_key)


def create_key(access_key, secret_key):
    r = redis.Redis(host=auth_redis['host'], port=auth_redis['port'], db=auth_redis['db'])
    r.set(access_key, secret_key)


def base64_url_decode(inp):
    # 通过url传输时去掉了=号，所以需要补上=号
    return base64.urlsafe_b64decode(str(inp + '=' * (4 - len(inp) % 4)))


def check_jwt(jwt_code):
    try:
        jwt_list = jwt_code.split('.')
        if len(jwt_list) == 3:
            h, p, s = jwt_list
            headers = base64.b64decode(h)
            crypt_type = json.loads(headers).get('alg', None)
            if crypt_type:
                payload = base64_url_decode(p)
                access_key = json.loads(payload).get('accesskey', None)
                if access_key:
                    secret_key = get_key(access_key)[0]
                    if secret_key:
                        payload = jwt.decode(jwt_code, secret_key, algorithms=crypt_type)
                        return True, payload
                    else:
                        return False, "jwt payload error key"
                else:
                    return False, 'jwt payload error'
            else:
                return False, 'jwt headers error'
        else:
            return False, 'jwt code error'
    except Exception as error:
        return False, str(error)


def jwt_auth(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        jwt_code = func_args['self'].get_argument('jwt', strip=True)
        jwt_stat, jwt_res = check_jwt(jwt_code)
        return f(func_args['self'], jwt_res)
    return wrapper


if __name__ == '__main__':
    create_key('wangyazhe', '1234567890')


