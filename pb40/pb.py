c = ''
i = 1

while len(c) < 1000000:
	c = c + str(i)
	i += 1

print int(c[0]) * int(c[9]) * int(c[99]) * int(c[999]) * int(c[9999]) * int(c[99999]) * int(c[999999])
