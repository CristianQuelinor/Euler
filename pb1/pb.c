#include <stdio.h>

int main(int argc, char* argv[])
{
	int i, somme = 0;

	for(i = 0 ; i < 1000 ; i++) {
		if(i % 3 == 0 || i % 5 == 0) {
			somme += i;
		}
	}

	printf("%d\n", somme);
	return 0;
}
