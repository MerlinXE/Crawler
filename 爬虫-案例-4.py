from bs4 import BeautifulSoup
import requests

url = "http://www.google.com.hk"
r = requests.get(url)
print(r.status_code)
demo = r.text

soup = BeautifulSoup(demo, "html.parser")

print(type(soup.a.string))

