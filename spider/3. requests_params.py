import requests

# url = "https://www.baidu.com/s?wd=python"
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
# }
#
# response = requests.get(url, headers=headers)
# with open("baidu.html", "wb") as f:
#     f.write(response.content)


url = "https://www.baidu.com/s?"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
}
data = {
    "wd": "python"
}

response = requests.get(url, headers=headers, params=data)
print(response.url)
with open("baidu1.html", "wb") as f:
    f.write(response.content)
