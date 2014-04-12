nb = 0

units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
u = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
dozens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy' 'eighty', 'ninety']
d = [100, 100, 100, 100, 100, 100, 100, 100]
specials = ['and', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
s = [891, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
hundreds = ['onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']
h = [100, 100, 100, 100, 100, 100, 100, 100, 100]

for i, hundred in enumerate(hundreds):
	nb += h[i]*len(hundred)

for i, special in enumerate(specials):
	nb += s[i]*len(special)

for i, dozen in enumerate(dozens):
	nb += d[i]*len(dozen)

for i, unit in enumerate(units):
	nb += u[i]*len(unit)

# On rajoute one thousand
nb += len('onethousand')

print nb
