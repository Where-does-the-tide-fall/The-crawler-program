import json
import requests

url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Referer": "https://movie.douban.com/",
}

response = requests.get(url, headers=headers)
json_str = response.content.decode()
ret1 = json.loads(json_str)
print(ret1)

with open('douban.txt', "w", encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False, indent=2))
