from parse import parse_url
import json


class DoubanSpider:

    def __init__(self):
        # self.temp_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%AC%A7%E7%BE%8E&sort=recommend&page_limit=20&page_start=40"
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?start={}&count=18&loc_id=108288"

    def get_contentf_list(self, html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data['total']
        return content_list, total

    def save_content_list(self, content_list):
        with open('douban.json', 'a', encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                # f.write("\n")

    def run(self):  # 实现主要逻辑
        num = 0
        total = 30
        while num < total + 18:
            # 1. start_url
            start_url = self.temp_url.format(num)
            # 2. 发送请求,获取响应
            html_str = parse_url(start_url)
            # 3. 提取数据
            content_list = self.get_contentf_list(html_str)

            # 4. 保存
            self.save_content_list(content_list)
            # 5. 构造下一页的url地址, 循环以上操作
            num += 18


if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()
