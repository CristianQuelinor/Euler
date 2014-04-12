nb_ways = 0
change = 200

for a in range(0, change + 1, 200):
	change = 200 - a
	for b in range(0, change + 1, 100):
		change = 200 - a - b
		for c in range(0, change + 1, 50):
			change = 200 - a - b - c
			for d in range(0, change + 1, 20):
				change = 200 - a - b -c - d
				for e in range(0, change + 1, 10):
					change = 200 - a - b - c - d - e
					for f in range(0, change + 1, 5):
						change = 200 - a - b - c - d - e - f
						for g in range(0, change + 1, 2):
							change = 200 - a - b - c - d - e - f - g

							if a + b + c + d + e + f + g <= 200:
								nb_ways += 1 # there is now only one way to make 2 pounds

print nb_ways
