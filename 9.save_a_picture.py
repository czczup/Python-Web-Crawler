import requests
import os
url = "https://p1.ssl.qhimg.com/t0151320b1d0fc50be8.png"
root = "D://picss//"
path = root + url.split('/')[-1]
try:
    #判断根目录是否存在
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
