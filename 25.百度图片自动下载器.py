import requests
import os
#技术路线:requests

#用百度图片搜索关键词
def SearchInBaidu():
    params = {
        'tn' : 'resultjsonavatarnew',
        'ie' : 'utf-8',   #文字编码
        'cg' : '',
        'itg' : '',
        'z' : '0',
        'fr' : '',
        'width' : '',
        'height' : '',
        'lm' : '-1',
        'ic' : '0',
        's' : '0',
        'word' : word,    #搜索关键词
        'st' : '-1',
        'gsm' : '',
        'rn' : '30',      #每页多少张图片
        'pn' : ''         #页数
        }
    for page in range(1,pages+1):       #从第1页到pages页爬取图片
        params['pn'] = str(page)
        getResponse(params)                


#向百度发出请求并取得图片的URL
def getResponse(param,code='utf-8'):
    url = 'http://image.baidu.com/search/avatarjson'
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,params=param,headers = kv)
    r.raise_for_status()
    r.encoding = code
    json = r.json()['imgs']

    for i in range(len(json)):
        Download_Pictures(json[i]['objURL'])    #下载json中对应的URL
        count[0] = count[0] + 1
        print('\r当前进度: {:.2f}%'.format(count[0]*100/(len(json)*pages)),end='')
        #生成动态进度条

#从图片原网址下载图片
def Download_Pictures(url):
    root = address +r'\%s'%word                 #为每一个关键词建立根目录
    if not os.path.exists(root):                #若不存在则创建目录
        os.makedirs(root)
    try:
        filepath = os.path.join(root,'%d.jpg'%(count[1]+1))
        r = requests.get(url,timeout=1)         #下载每张图片
        r.raise_for_status()
        with open(filepath,'wb') as f:          #保存图片
            f.write(r.content)
            f.close()
            count[1] = count[1] + 1
    except:                                     #若下载失败则跳过
        return ""
if __name__ == '__main__':
    #爬虫所需的三个参数
    word = input("请输入搜索关键词:")
    pages = eval(input("请输入爬取页数:"))
    address = input('请输入储存路径:')
    count = [0,0]
    #count[0]记录进度,count[1]记录爬取成功数
    SearchInBaidu()
    print('\n成功下载%d张图片'%count[1])
