import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
parms = dict()
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count:', len(info['comments']))
sum_=0
for item in info['comments']:
    sum_=sum_+int(item['count'])
print('Sum:',sum_)
