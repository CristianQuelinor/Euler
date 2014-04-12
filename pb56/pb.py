max_digital_sum = 0

for a in range(2, 100):
	for b in range(2, 100):
		n = a**b
		sum = 0

		for m in str(n):
			sum += int(m)

		if sum > max_digital_sum:
			max_digital_sum = sum

print max_digital_sum
