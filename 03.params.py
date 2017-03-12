Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> kv = {'key1':'value1','key2':'value2'}
>>> import requests
>>> r = requests.request('GRT','http://python123.io.ws')
print
>>> print(r.url)
http://python123.io.ws/
>>> r = requests.request('GRT','http://python123.io.ws',params=kv)
>>> print(r.url)
http://python123.io.ws/?key1=value1&key2=value2
>>> 
