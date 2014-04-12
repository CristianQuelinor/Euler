#include <stdio.h>

int main(int argc, char* argv[])
{
	unsigned long int a = 1, b = 2, somme = 0, tmp;

	while(a < 4000000) {
		if(a % 2 == 0) {
			somme += a;
		}

		tmp = a + b;
		a = b;
		b = tmp;
	}

	printf("%lu\n", somme);
	return 0;
}
