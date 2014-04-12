#include <stdio.h>
#include <math.h>

int pgcd(int a, int b){
	int retour;

	while (a != 0 && b != 0) {
		if (a > b) {
			a = a - b;
		}
		else {
			b  = b - a;
		}
	}

	if (a == 0) {
		retour =  b;
	}
	else {
		retour = a;
	}

	return retour;
}

int ppcm(int a, int b){

	return a/pgcd(a, b)*b;
}

int main(int argc, char* argv[])
{
	int i, m = 1;

	for(i = 1 ; i < 20 ; i++) {
		m = ppcm(m, i);
	}

	printf("%d\n", m);

	return 0;
}

