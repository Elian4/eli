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
print(d)
'''minimum = None
maximum = None
mkey = ''
maxkey = ''
for key in d:
	if minimum is None or d[key] < minimum:
		minimum=d[key]
		#key = mkey
	if maximum is None or d[key] > maximum:
		maximum=d[key]
		#key = maxkey
print(maximum)'''