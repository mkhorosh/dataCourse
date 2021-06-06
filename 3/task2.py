import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def func(name):
    url = name
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    flag = 0
    for tag in tags:
        flag += 1
        if (flag == 18):
            print(tag.get('href', None))
            return tag.get('href', None)


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = func('http://py4e-data.dr-chuck.net/known_by_Thea.html')
for i in range(0,6):
    url = func(url)
