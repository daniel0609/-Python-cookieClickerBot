r = "456.789 billion"
num = ''
mul = 0
num.join("asd")
for x in r:
	if(x.isdigit() or x=='.'):
		num=num+x
		print(x)
	if(x=='m'):
		mul=1000000
	elif(x=='b'):
		mul=1000000000
print (float(num)*mul)