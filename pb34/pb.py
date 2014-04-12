factorials = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}
sum = 0

def is_curious(n):
	local_sum = 0

	for number in str(n):
		local_sum += factorials[number]

	if local_sum == n:
		return True
	else:
		return False

for i in range(3, 10000000):
	if is_curious(i) == True:
		sum += i

print sum
