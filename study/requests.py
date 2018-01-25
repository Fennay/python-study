#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import ssl

from urllib.request import Request
from urllib.request import urlopen

context = ssl._create_unverified_context()
url = 'https://foofish.net/pip.html'

request = Request(url=url, method='GET', headers={"Host": "foofish.net"},
                  data=None)

response = urlopen(request,context=context)
headers = response.info()
context = response.read()
code = response.getcode()
