#encoding=utf-8

version = 0.1

import urllib
import urllib2
import time
import json
from hashlib import sha1


class CourierClient(object):

    API_HOST = 'http://sms.toraysoft.com'

    def __init__(self, app, key, host=None):
        self.app = app
        self.key = key
        self.host = host or self.API_HOST

    def get_request(self, url, params):
        params['ts'] = time.time()
        params['app'] = self.app
        keys = sorted(params.keys())
        src = '&'.join(['%s=%s' % (k, params[k]) for k in keys])
        src += self.key
        sign = sha1(src).hexdigest()
        params['sign'] = sign
        query = urllib.urlencode(params)
        rsp = urllib2.urlopen(self.host + url + '?' + query).read()
        print rsp
        return json.loads(rsp)

    def get_code(self, mobile, code=None, expire=0):
        """发送一个校验验，不指定则让courier随机生成。
        """
        params = {'mobile': mobile, 'expire': expire}
        if code:
            params['code'] = code
        rsp = self.get_request('/code/', params)
        return rsp['code']

    def verify_code(self, mobile, code):
        """验证一个校验码。
        """
        rsp = self.get_request('/verify/', {'mobile': mobile, 'code': code})
        return rsp['valid']
