'''translate'''
'''休眠'''

import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入需要翻译的内容(输入"q!"退出程序):')
    if content == 'q!':
        break
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    # # 隐藏 ---- 1
    # head = {}
    # head['User-Agent'] ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

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
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    req = urllib.request.urlopen(req)
    html = req.read().decode('utf-8')
    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']
    print(f'翻译结果:{target}')
    time.sleep(5)
