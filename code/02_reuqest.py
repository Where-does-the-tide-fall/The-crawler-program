# import requests
#
# url = 'https://fanyi.baidu.com/langdetect'
#
# data = {"query": "你好",
#         "from": "zh",
#         "to": "en",
#         # "token": "147f6352e77142b2461e8e41bd2fef5e",
#         # "sign": "265461.61380"
#         }
# headers = {
#     "User-Agent": "'User-Agent': 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
#     # "Referer": "https://fanyi.baidu.com/",
#     # "Host": "fanyi.baidu.com",
#     # "Origin": "https: // fanyi.baidu.com"
# }
# response = requests.post(url, data=data, headers=headers)
# print(response)
#
# print(response.content.decode())
#
#

# from urllib import request, parse
# import json
#
#
# def translate(content):
#     url = "http://fanyi.baidu.com/sug"
#     data = parse.urlencode({"kw": content})  # 将参数进行转码
#     headers = {
#         'User-Agent': 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10'
#     }
#     req = request.Request(url, data=bytes(data, encoding="utf-8"), headers=headers)
#     r = request.urlopen(req)
#     print(r.code) #查看返回的状态码
#     html = r.read().decode('utf-8')
#     # json格式化
#     html = json.loads(html)
#     print(html)
#     for k in html["data"]:
#         print(k["k"], k["v"])
#
#
# if __name__ == '__main__':
#     content = input("请输入您要翻译的内容：")
#     translate(content)


# -*- coding: UTF-8 -*-
# @author: caoyang
# @email: caoyang@163.sufe.edu.cn

import json
import requests

word = input("请输入您要输入的中文:")
url = 'https://fanyi.baidu.com/langdetect'
data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'simple_means_flag': '3',
    'sign': '183948.404925',
    'token': '36fffe666423ac015ff58d7f3a9bc433',
    'domain': 'common',
}
headers = {
    'Host': 'fanyi.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '116',
    'Origin': 'https://fanyi.baidu.com',
    'Connection': 'keep-alive',
    'Referer': 'https://fanyi.baidu.com/',
    'Cookie': 'BAIDUID=DBBD7E00FF1E064D7FC01E585DC97E13:FG=1; BIDUPSID=DBBD7E00FF1E064D7FC01E585DC97E13; PSTM=1612755445; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; delPer=0; PSINO=5; H_PS_PSSID=33425_33442_33260_33272_33571_33585_33318_33268; BA_HECTOR=0184al2la1ak8421rh1g21cfm0r; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BCLID=10815360212121519601; BDSFRCVID=z2kOJexroG3VnU3eKBZghcyL2LweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF326DfXP6-hnjy3b7pWfKb5lvIoR3d-nrdDxAWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqCLaMItR3f; __yjs_duid=1_386a6866632fadafb73dffc74e18bbf91612755447272; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1612755447; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1612755466; ab_sr=1.0.0_M2E2ZWQ0NDdkMTQyMTFiYTRjY2Y1NDIxOGNhZmVmZmEyMjE3YTY0MmE0OTdiNWQ4NjQxMDQzNDYxMzVjNDA2NzY5MWU4NTRiMjY1MDdlYWUzYjk4YjNmZDRhYmI4MGQw; __yjsv5_shitong=1.0_7_9ec8cc04516309efce46e669dcc80c158b7f_300_1612755466482_114.230.179.127_9723e5b1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1',
}

response = requests.post(url, data=data, headers=headers)
print(response)

print(response.content.decode())

