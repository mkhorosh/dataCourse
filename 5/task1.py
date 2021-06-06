import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_1241705.json'
data = urllib.request.urlopen(url).read()

info = json.loads(data)
sum = 0
for item in info["comments"]:
    sum += int(item["count"])
print(sum)