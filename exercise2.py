fhandle = open('mbox.txt')
d = dict()
for line in fhandle:
	line = line.rstrip()
	if not line.startswith('From '):
		continue
	words = line.split()
	day = words[2]
	if day not in d:
		d[day] = 1
	else:
		d[day]+=1
print(d)