import math

triangle = []

file = open("triangle", "r")

for line in file:
	list_str = line.split(' ')
	list_int = []

	for element in list_str:
		list_int.append(int(element))

	triangle.append(list_int)

file.close()

l = len(triangle)
j = l - 1

for i in range(1, l):	
	for k in range(0, len(triangle[j - 1])):
		maxi = max(triangle[j][k], triangle[j][k + 1])
		triangle[j - 1][k] += maxi

	j -=  1

print triangle[0][0]
