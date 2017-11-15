import urllib
import urllib2
 
values={}
values['username'] = "805043442@qq.com"
values['password']="wy980913.."
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
