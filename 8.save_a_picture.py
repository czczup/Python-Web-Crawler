Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> path = "D:/abc.jpg"
>>> url = "https://p1.ssl.qhimg.com/t0151320b1d0fc50be8.png"
>>> r = requests.get(url)
>>> r.status_code
200
>>> with open(path,'wb') as f:
	f.write(r.content)

	
5471
>>> f.close()
>>> 
