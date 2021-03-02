import urllib.request
# import urllib.error

request = urllib.request.urlopen('http://www.fishc.com')
html = request.read()
html = html.decode('utf-8')
print(html)


