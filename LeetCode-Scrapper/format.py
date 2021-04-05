f1 = open('hard','r')
f2 = open('hardf','w')
for line in f1:
	if ')' in line and '|' in line:
		f2.write('-----------------------------------------------------------------------------------\n')
	if line == '\n':
		continue
	f2.write(line)