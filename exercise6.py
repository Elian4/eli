fhandle = open('mbox.txt','r')
d = dict()
for line in fhandle:
	lines = line.rstrip()
	if lines.startswith('From '):
		atpos = lines.find('@')
		pos = lines.find(' ',atpos)
		mail = lines[atpos+1:pos]
		if not  mail in d:
			d[mail] = 1
			continue
		else:
			d[mail]+=1
print(d)