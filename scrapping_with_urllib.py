import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter')
    
uh = urllib.request.urlopen(url, context=ctx)


content=uh.read().decode()


count=0
no=re.findall('[0-9]+',content)

for nos in no:
    count=count+int(nos)
print(count-9)    
    
    


            
        
