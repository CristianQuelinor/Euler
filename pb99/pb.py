import math

def solution():
	base_exp = open('base_exp.txt', 'r')
	exps = []

	for line in base_exp:
		exp = line.split(',')
		exps.append([int(exp[0]), int(exp[1])])

	base_exp.close()

	(log_a_max, b_max) = (math.log(exps[0][0]), exps[0][1])
	line_max = 1

	for line, exp in enumerate(exps):
		if log_a_max * b_max < math.log(exp[0]) * exp[1]:
			line_max = line
			log_a_max = math.log(exp[0])
			b_max = exp[1]

	return line_max + 1

print solution()
