import json

import requests

url = 'https://fanyi.baidu.com/langdetect'

data = {"query": "你好",
        "from": "zh",
        "to": "en",
        # "token": "147f6352e77142b2461e8e41bd2fef5e",
        # "sign": "265461.61380"
        }
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    # "Referer": "https://fanyi.baidu.com/",
    # "Host": "fanyi.baidu.com",
    # "Origin": "https: // fanyi.baidu.com"
}
response = requests.post(url, data=data, headers=headers)
heml_str = response.content.decode()   # json字符串

dict_ret = json.loads((heml_str))


print(dict_ret)

print(type(dict_ret))
