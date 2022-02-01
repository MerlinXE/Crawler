import requests
import bs4

col: int = 5
print(col)


def getContent(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        print(r.raise_for_status())
        r.raise_for_status()
        print("成功")
        print(r.request.headers)
        print(r.headers)
    except:
        print("连接异常")


if __name__ == "__main__":
    url = "http://www.baidu.com"

    getContent(url)
