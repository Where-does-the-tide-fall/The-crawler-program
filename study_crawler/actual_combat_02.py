'''有道有反爬虫'''
'''translate'''

import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容:')
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '16127787977133'
data['sign'] = '4d6a49f6f8bedd3573e9c5ccac901543'
data['lts'] = '1612778797713'
data['bv'] = '4f7ca50d9eda878f3f40fb696cce4d6d'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
target = json.loads(html)
print(f'翻译结果:{target}')
