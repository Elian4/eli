fhandle = open('mbox.txt')
d = dict()
d2 = dict()
for line in fhandle:
	line = line.rstrip()
	if not line.startswith('From '):
		continue
	words = line.split()
	day = words[1]
	if day not in d:
		d[day] = 1
	else:
		d[day]+=1
maximum = None
for key in d:
	if not (maximum is None or d[key] > maximum):
		continue
	maximum=d[key]
	print(key,maximum)