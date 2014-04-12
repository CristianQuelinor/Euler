import math

def is_abundant(n):
	r = int(math.sqrt(n)) + 2

	E1 = [i for i in range(2, r) if n % i == 0]
	E2 = [n / i for i in E1]

	divisors = E1 + E2
	divisors = set(divisors)

	divisors_sum = sum(divisors) + 1

	if divisors_sum > n:
		return True
	else:
		return False

abundants = [i for i in range(12, 28124) if is_abundant(i)]

abundants_sum = set([])

for i in range(len(abundants)):
		for j in range(i, len(abundants)):
			local_sum = abundants[i] + abundants[j]

			if local_sum > 28123:
				break
			else:
				abundants_sum.add(local_sum)

non_abundants_sum = 395465626 - sum(abundants_sum)

print non_abundants_sum
