import requests

url = "http://www.renren.com/917697177/newsfeed/photo"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}

cookie = "anonymid=klj8n7lu87azbp; depovince=GW; _r01_=1; JSESSIONID=abcF7hQtaDZ-76TIqytFx; ick_login=05aecb4d-8a1f-494e-a6b2-52349ffa5145; taihe_bi_sdk_uid=5dbfde797ec96615733725b68a471128; taihe_bi_sdk_session=1393d110db3579567d0220b834153af6; loginfrom=null; wp_fold=0; t=136f93672d11dcd64a87328130f2ea7b7; societyguester=136f93672d11dcd64a87328130f2ea7b7; id=917697177; xnsid=2c8af3b0; jebecookies=f8d84f95-e5bf-4c6c-9aa2-148bc0f55b7f|||||"

cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}

print(cookie_dict)

response = requests.get(url, headers=headers, cookies=cookie_dict)

with open("renren2.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())
