import requests
from lxml import etree
import json


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }

    def get_url_list(self):  # 根据url地址的规律, 构造url list
        url_list = [self.url_temp.format(i) for i in range(1, 14)]
        return url_list

    def parse_url(self, url):
        print('now url:', url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):  # 3. 提取数据
        html = etree.HTML(html_str)
        # 1. 分组
        div_list = html.xpath("//div[@class = 'col1 old-style-col1']/div")
        # print(div_list)
        content_list = []
        for div in div_list:
            item = {}
            item["author_name"] = div.xpath(".//a/h2/text()")[0].strip() if len(div.xpath(".//a/h2/text()")) > 0 else None
            item["content"] = div.xpath(".//div[@class='content']//text()")
            item["content"] = [i.strip() for i in item["content"]]
            item["stats-vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")[0] if len(
                div.xpath(".//span[@class='stats-vote']/i/text()")) > 0 else None
            item["stats-comments"] = div.xpath(".//span[@class='stats-comments']/a/i/text()")[0] if len(
                div.xpath(".//span[@class='stats-comments']/a/i/text()")) > 0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):  # 保存
        with open("qiubai.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1. 根据url地址的规律, 构造url list
        url_list = self.get_url_list()
        # 2.发送请求,获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 提取数据
            content_list = self.get_content_list(html_str)
            # 保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()
