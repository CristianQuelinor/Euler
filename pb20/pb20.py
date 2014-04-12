fact = 1

for i in range(1, 101):
	fact *= i

fact = str(fact)
sum = 0

for number in fact:
	sum += int(number)

print sum
