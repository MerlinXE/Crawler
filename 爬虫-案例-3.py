import requests
import os
import PyQt5



"""
#抓取网上图片
filepath = "C:/Users/Administrator/PycharmProjects/网页爬"
print(os.path.exists(filepath))

url ="https://gimg2.baidu.com/image_search/9150307-8.jpg"
s = url.split("/")[-1]
print(s)
"""

"""
#抓取网上图片
class MyEs:
    @property
    def getTarget(self):
        url = "https://youtu.be/ZMjhBB17KVY?t=5526"
        des = "2.mp4"
        r = requests.get(url)
        print(r.status_code)
        print(r.encoding)
        print(r.apparent_encoding)
        print(r.content[:100])
        print(r.text[:100])

        with open(des, "wb") as f:
            f.write(r.content)


s = MyEs()
s.getTarget
"""

fromfile = "a1 (3).mp4"
tofile = "bb.mp4"
# TODO: FDS
with open(fromfile, "rb") as ff:
    tocontent = ff.read()
    print(tocontent[-100:])

with open(tofile, "wb") as tf:
    tf.write(tocontent)



