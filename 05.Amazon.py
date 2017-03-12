Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> r = requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
>>> r.status_code
503
>>> r.encoding
'ISO-8859-1'
>>> r.encoding = r.apparent_encoding
>>> r.text
'<!--\n        To discuss automated access to Amazon data please contact api-services-support@amazon.com.\n        For information about migrating to our APIs refer to our Marketplace APIs at https://developer.amazonservices.com.cn/index.html/ref=rm_5_sv, or our Product Advertising API at https://associates.amazon.cn/gp/advertising/api/detail/main.html/ref=rm_5_ac for advertising use cases.\n-->\n<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><title>亚马逊</title><body style="text-align:center;"><br><div style="width:600px;margin:0 auto;text-align:left;"><h2>意外错误</h2></div><br><div style="width:500px;margin:0 auto;text-align:left;"><font color="red">报歉，由于程序执行时，遇到意外错误，您刚刚操作没有执行成功，请稍后重试。或将此错误报告给我们的客服中心：<a href="mailto:service_bj@cs.amazon.cn">service_bj@cs.amazon.cn</a></font><br><br>推荐您<a href="javascript:history.back(1)">返回上一页</a>，确认您的操作无误后，再继续其他操作。<br>您可以通过亚马逊<a href="http://www.amazon.cn/help/ref=cs_503_link/" target="_blank">帮助中心</a>，获得更多的帮助。<br></div></body></html>\ufeff'
>>> r.request.headers
{'User-Agent': 'python-requests/2.13.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
>>> kv = {'user-agent':'Mozilla/5.0'}
>>> url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
>>> r = requests.get(url,headers = kv)
>>> r.status_code
200
>>> r.request.headers
{'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
>>> r.text[:1000]
'\n\n\n  \n  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    <!doctype html><html class="a-no-js" data-19ax5a9jf="dingo">\n    <head>\n<script type="text/javascript">var ue_t0=ue_t0||+new Date();</script>\n<script type="text/javascript">\nvar ue_hob=+new Date();\nvar ue_id=\'WR5Y5NRMNDSDHXAHB6PY\',\nue_csm = window,\nue_err_chan = \'jserr-rw\',\nue = {};\n(function(d){var e=d.ue=d.ue||{},f=Date.now||function(){return+new Date};e.d=function(b){return f()-(b?0:d.ue_t0)};e.stub=function(b,a){if(!b[a]){var c=[];b[a]=function(){c.push([c.slice.call(arguments),e.d(),d.ue_id])};b[a].replay=function(b){for(var a;a=c.shift();)b(a[0],a[1],a[2])};b[a].isStub=1}};e.exec=function(b,a){return function(){if(1==window.ueinit)try{return b.apply(this,arguments)}catch(c){ueLogError(c,{attribution:a||"undefined",logLevel:"WARN"})}}}})(ue_csm);\n\nue.stub(ue,"log");ue.stub(ue,"onunload");ue.stub(ue,"onflush");\n\n(function(c,d){function e(f,b){if(!(a.ec>a.mxe)&&f){a.ec++;a.te'
>>> 
