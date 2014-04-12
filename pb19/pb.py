import math

# Paramameters (day of is of January, year)
# Returns (number of sundays, day of 1st of January of next year)
def nb_sundays_year(day, year):
	nb_sundays = 0

	# January
	if day == 6:
		nb_sundays += 1

	day += 3
	day %= 7

	# February
	if day == 6:
		nb_sundays += 1

	if year % 4 == 0:
		day += 1
		day %= 7

	# March
	if day == 6:
		nb_sundays += 1

	day += 3
	day %= 7

	# April
	if day == 6:
		nb_sundays += 1

	day += 2
	day %= 7

	# May
	if day == 6:
		nb_sundays += 1

	day += 3
	day %= 7

	# June
	if day == 6:
		nb_sundays += 1

	day += 2
	day %= 7
	
	# July
	if day == 6:
		nb_sundays += 1

	day += 3
	day %= 7

	# August
	if day == 6:
		nb_sundays += 1

	day += 3
	day %= 7

	# September
	if day == 6:
		nb_sundays += 1

	day += 2
	day %= 7

	# October
	if day == 6:
		nb_sundays += 1

	day += 3
	day %= 7

	# November
	if day == 6:
		nb_sundays += 1

	day += 2
	day %= 7

	# December
	if day == 6:
		nb_sundays += 1

	day += 3
	day %= 7

	return (nb_sundays, day)

nb_sundays = 0
day = 1

for year in range(1901, 2001):
	(nb_sundays_result, day_result) = nb_sundays_year(day, year)
	nb_sundays += nb_sundays_result
	day = day_result

print nb_sundays
