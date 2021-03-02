'''translate'''
'''代理'''

import urllib.request
import urllib.parse
import random

url = 'http://www.whatismyip.com.tw'
ip_list = ['42.243.181.2:4245', '222.221.85.152:4240', '171.110.55.151:4256']


proxy_support = urllib.request.ProxyHandler({'http': random.choice(ip_list)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')]

urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
