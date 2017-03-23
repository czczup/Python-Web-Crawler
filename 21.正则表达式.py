>>> import re
>>> match = re.search(r'[1-9]\d{5}','BIT 100081')
>>> if match:
	print(match.group(0))

	
100081
#search函数和group(0)方法的运用


>>> match = re.match(r'[1-9]\d{5}','BIT 100081')
>>> match
>>> if match:
	print(match.group(0))

	
>>> match.group(0)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    match.group(0)
AttributeError: 'NoneType' object has no attribute 'group'
>>> match = re.match(r'[1-9]\d{5}','100081 BIT')
>>> if match:
	match.group(0)

	
'100081'
#match函数的运用




>>> ls = re.findall(r'[1-9]\d{5}','BIT 100081 TSU100084')
>>> ls
['100081', '100084']
>>> re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
['BIT', ' TSU', '']
>>> re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
['BIT', ' TSU100084']

>>> for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
	if m:
		print(m.group(0))

		
100081
100084
#findall函数的运用



>>> re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084')
'BIT:zipcode TSU:zipcode'
>>> type(match)
<class '_sre.SRE_Match'>
>>> 
#sub函数的运用
