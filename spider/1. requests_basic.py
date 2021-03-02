import requests

url = "http://www.baidu.com"

response = requests.get(url)

response.encoding = "utf8"
# 打印源码的str数据类型
# print(response.text)
# print(response.encoding)

# response.content是存储bytes类型的响应源码, 可以进行decode操作
# print(response.content.decode())


# 常见的相应对象参数和方法
# 响应url
# print(response.url)

# 状态码
# print(response.status_code)

# 响应对应的请求头
# print(response.request.headers)

# 响应头
# print(response.headers)

# 打印响应设置cookies
print(response.cookies)