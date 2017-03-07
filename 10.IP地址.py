Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> url = "http://m.ip138.com/ip.asp?ip="
>>> r = requests.get(url + '202.204.80.112')
>>> r.status_code
200
>>> r.text[-500:]
'value="查询" class="form-btn" />\r\n\t\t\t\t\t</form>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="query-hd">ip138.com IP查询(搜索IP地址的地理位置)</div>\r\n\t\t\t\t<h1 class="query">您查询的IP：202.204.80.112</h1><p class="result">本站主数据：北京市海淀区 北京理工大学 教育网</p><p class="result">参考数据一：北京市 北京理工大学</p>\r\n\r\n\t\t\t</div>\r\n\t\t</div>\r\n\r\n\t\t<div class="footer">\r\n\t\t\t<a href="http://www.miitbeian.gov.cn/" rel="nofollow" target="_blank">沪ICP备10013467号-1</a>\r\n\t\t</div>\r\n\t</div>\r\n\r\n\t<script type="text/javascript" src="/script/common.js"></script></body>\r\n</html>\r\n'
>>> 
