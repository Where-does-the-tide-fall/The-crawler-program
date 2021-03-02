from retrying import retry
import requests

"""
专门请求url地址的方法
"""
# 这是电脑版的  手机版需要修改
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Referer": "https://m.douban.com/app_topic/tv_american",
}


@retry(stop_max_attempt_number=3)  # 让被装饰得函数反复执行三次, 三次全部错误才会报错, 中间有一次正常, 程序就继续往下走
def _parse_url(url):
    print('*' * 100)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url)[:100])
