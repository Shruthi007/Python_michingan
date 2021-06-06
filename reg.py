import re
handle=open('testsub.txt')
essay=handle.read()
lis=re.findall('[0-9]+',essay)
s=0
for n in lis:
     s=s+int(n)
print(s)
