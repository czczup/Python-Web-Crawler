Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> r = requests.get("http://python123.io/ws/demo.html")
>>> demo = r.text
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo,"html.parser")
>>> for link in soup.find_all('a'):
	print(link.get('href'))

	
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
>>> 
