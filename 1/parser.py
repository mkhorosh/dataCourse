import re

text = open('regex_sum_1241700.txt','r')
lines = text.readlines()
sum = 0
for l in lines:
	digits = re.findall('[0-9]+',l)
	if(len(digits)!=0):
		for i in digits:
			sum += int(i)
print(sum)
