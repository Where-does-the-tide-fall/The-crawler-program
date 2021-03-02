import requests

url = "http://www.baidu.com"

response = requests.get(url)

print(len(response.content.decode()))
print(response.content.decode())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
}

response1 = requests.get(url, headers=headers)

print(len(response1.content.decode()))
print(response1.content.decode())