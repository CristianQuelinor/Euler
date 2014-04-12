#include <stdio.h>

int main(int argc, char* argv[])
{
	int i;
	unsigned long int a = 0, b = 0;

	for(i = 1 ; i <= 100 ; i++) {
		a += i*i;
		b += i;
	}

	b *= b;

	printf("%lu\n", b - a);

	return 0;
}

