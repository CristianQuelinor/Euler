powers = {0:0, 1:1, 2:2**5, 3:3**5, 4:4**5, 5:5**5, 6:6**5, 7:7**5, 8:8**5, 9:9**5}
sum = 0

for number in range(2, 5*(9**5) + 1):
	tmp = number
	e = number % 10
	tmp -= e
	d = tmp/10 % 10
	tmp -= 10*d
	c = tmp/100 % 10
	tmp -= 100*c
	b = tmp/1000 % 10
	tmp -= 1000*b
	a = tmp/10000 % 10
	alpha = tmp/100000 % 10

	alpha, a, b, c, d, e = powers[alpha], powers[a], powers[b], powers[c], powers[d], powers[e]
	
	if alpha + a + b + c + d + e == number:
		print number
		sum += number

print sum
