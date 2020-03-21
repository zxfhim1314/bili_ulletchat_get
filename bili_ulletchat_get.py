import requests
from bs4 import BeautifulSoup
from xlwt import *

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


# https://api.bilibili.com/x/web-interface/view?aid=89441613
# https://api.bilibili.com/x/v1/dm/list.so?oid=152796906
# av89441613

def save_data(aid, data):
    name = aid + ".xls"
    file = Workbook(encoding="utf-8")
    table = file.add_sheet("date", True)

    top = ["弹幕", "数量"]
    table.write(0, 0, top[0])
    table.write(0, 1, top[1])
    x = 1
    for key, value in data.items():
        table.write(x, 0, key)
        table.write(x, 1, value)
        x += 1
    file.save(name)


def bili_ullstchct():
    aid = input("av:")
    uri1 = "https://api.bilibili.com/x/web-interface/view?aid=" + aid
    req = requests.get(uri1, headers=head).json()
    cid = req["data"]["cid"]
    print(cid)
    uri2 = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + str(cid)
    req = requests.get(uri2, headers=head).content.decode("utf-8")
    print(req)
    soup = BeautifulSoup(req, "html.parser")
    print(soup.i)
    a = 0
    dtxt = {}
    for x in soup.i.find_all("d"):
        print(x.string)
        x = x.string
        a += 1
        if dtxt.__contains__(x):
            dtxt[x] = dtxt[x] + 1
        else:
            dtxt[x] = 1
    print("弹幕数：" + str(a))
    save_data(aid, dtxt)

if __name__ == "__main__":
    while True:
        bili_ullstchct()
