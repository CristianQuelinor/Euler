def is_palindromic(n):
	string = str(n)
	
	if string == string[::-1]:
		return True
	else:
		return False

def dec2bin(dec):
	bin = ''

	while dec != 0:			
		bin = str(dec & 1) + bin
		dec  >>= 1
	return bin

somme = 0

for i in range(1, 1000001):
	if is_palindromic(i) == True and is_palindromic(dec2bin(i)) == True:
		somme += i

print somme
