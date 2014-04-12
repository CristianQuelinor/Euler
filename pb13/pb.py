sum = 0
fichier = open("numbers", "r")

for ligne in fichier:
	sum += int(ligne)

print str(sum)[0:10]

fichier.close()
