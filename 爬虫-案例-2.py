
import requests

"""#百度搜索关键词
url = "https://www.baidu.com/s"

kv = {"wd": "python"}
hd = {"user-agent": "Mozilla/5.0"}
r = requests.get(url, params=kv, headers=hd)
print(r.request.url)
print(r.status_code)
print(len(r.text))"""

#谷歌搜索关键词
url = "https://www.google.com/search"
kv = {"q": "pyqt5"}

r = requests.get(url, params=kv)
print(r.status_code)
