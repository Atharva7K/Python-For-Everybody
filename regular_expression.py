import re

file=open('sample.txt')

total=0
number=list()

content=file.read()

no=re.findall('[0-9]+',content)

for i in range(len(no)):
    no[i]=int(no[i])
print(sum(no))    

