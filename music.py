import requests
import re


url = "https://music.163.com/discover/toplist"
response = requests.get(url)
content = response.text
music_list = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', content)

print(len(music_list))


