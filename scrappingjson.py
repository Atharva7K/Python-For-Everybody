import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url=input('Enter')
    
uh = urllib.request.urlopen(url, context=ctx)


data=uh.read().decode()



info = json.loads(data)


count_list=info['comments']

cnt=0
for i in range(len(count_list)):
    count=count_list[i]['count']
    cnt=cnt+int(count)
    
print(cnt)    