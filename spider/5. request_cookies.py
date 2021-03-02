import requests

url = "https://github.com/Where-does-the-tide-fall"

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

# 构建cookie字典
temp = "_octo=GH1.1.1363837951.1602822217; _ga=GA1.2.845998210.1602822226; _device_id=2a2069518192a414ddf8a524b5ab51d3; tz=Asia%2FShanghai; has_recent_activity=1; user_session=A668po4_MrFHxVZmnEC1paLBZW_m1WSWsXP3F5Ivp1Xuxxqy; __Host-user_session_same_site=A668po4_MrFHxVZmnEC1paLBZW_m1WSWsXP3F5Ivp1Xuxxqy; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=Where-does-the-tide-fall; _gh_sess=WMTtAy6lJaqJSeJEauR6YVJWCQXhD3j5KtFenXS64oj8QsNysAwSrX7OZ4yWQQdC96hRsvnEQe3MfN13WFvBwdMslEoYSLPa5rK2Nsl%2BuMx3Xig%2F1tb4divkWs14Azwor3gydVt%2BxtgeDsVMeNFVf7okClgTIoNa%2FbxkR4kMeXHSVMAuSrbW6Gl6vAs8LPkiz4wOoEZ3z6yh2AoIQvxiJTp5jM22buy3fszgJ5NBHWMWuhuUxs%2BwDAYb8Ho36ThqWhY9ORoh%2FmKWqWRlOBIfXha6Z8ImeZDPrKhB5p6K9Sicuu3BWlljrJu%2B5ZHwv4gZB0%2FY5L0cE8qqQ%2BVKwMN9KQIBfE7%2FYrtggGh23TxrprUzlh7jH1B4r%2F0XreRiZzLanewy8%2FzPjKk4IqlvN6DSW9357a3mndogHVSZzpjakYVXiZko6DgmmoM54KD%2FbXK4Aqvi%2FSWnlOlJ21bTFdNm4IE3aOXt3BagfMAu1lRgKJJ8IHi4y%2BGrALxYma%2FIypuO37LgdFQ2lHS6DhLO0gAziug7a6xIO6pZyF6LttpWwKZpzZXlNCH2zdk4jjS31bhXDyae9zfYlueq1oV7hoSIoAoLUdynkJKlqpt2N28g%2FcswYm5Xrnavc47%2B7kiAC3lSShmThLwIU3JrzWlOOznAY%2Bv%2FdxmG%2FdhhzqbZ3lMAX%2FewsA3NQGpp8jNxZCdp3YSxZm%2BVAnNXfmdSuboafF%2FiVLUGrHY1t3PWVgQI%2BlA92yrupkekSSu68I3CG3rNeRmvQYeadghI5jUdc451YAMLgzAKrI6PubehMX%2FBNTFHFocZipZgkdfjTyBTPx%2FjHAXwlxC56RwNpAAblCE41CS%2FuoiuYwVWBrBXP78Te3OdkVLTuAU4J%2BoSJ83Qmr%2FJ5QxGh5k9FUje1pek5ABPzgAOj9%2BkbTVis6FjS8y%2Bt%2BkIx9leXLAgXVLxaTd7LpPkvYN8p3iJaP7iiyLEcqvKcLkuqSbN7dbewLWLO541TE82w%2FcgYOnp2ZQX2yVFJwCofgPtCprIRYV8qPJBXeH8WDtki0MSnH6zFTxXUu%2FAwhWwIiQu%2BCtJ03FLH4tmsRmwF06XqnSrdcYWe3obv0%2FnpEW5NwFIuadM6NXRqgXWGeq75xe9ie6Y9%2BXGgeC8t4%2Fgyc18MEva12Y65Nx21EM8tafPRXb4EEIK7mrO7Vf2ybt%2FehTpveT0AVna0D2SfrAOQgQeVng6EdajPC6eTFUY6egYg3pyaju4ygQEs9vI8wOWHdsN5O5WD1q7uR%2FlxCix%2B7mJ%2FSyiEiVs%2BfMrXzCZ7g%2FrlqL2U4ZMNZZtTB7l7ipnaPPZFUtSgPrDYskNKHhYCx9o%2FZJ2W2TxFH3DtPvtmNHNPO2SgVVcP0e8W4erbyTLUEXPBrRjxYc5iX35QlxXuvnsGzA4yUgVWoE3jpwOTclB5rZkWao%2F5VXO%2BHmchqWv17lOv4HyAZuQcePRB1372BfS5IBu4%2FhGr4F%2FXdzHtrxAFFO7ZqL%2FuGsedbWZHJKYtvvapbgK8%2FuPrUgMFfS%2BGR5ssMNtHSb50eR3ijdX--UJSRmOMveJTqamYa--%2BALm%2Bk57I%2FbtfeuxbJgS3g%3D%3D"

# 简单方法
cookie_list = temp.split(";")
cookies = {cookie.split("=")[0]: cookie.split("=")[-1] for cookie in cookie_list}
# cookies = {}
# for cookie in cookie_list:
#     cookies[cookie.split("=")[0]] = cookie.split("=")[-1]

print(cookies)

response = requests.get(url, headers=headers, cookies=cookies)

with open("github_w_cookies3.html", "wb") as f:
    f.write(response.content)
