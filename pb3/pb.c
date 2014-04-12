#include <stdio.h>
#include <math.h>

void facteurs_premiers(unsigned long int a) {
	unsigned long int divider = (unsigned long int)floor(sqrt(a));

	if(a != 1) {
		while(a % divider != 0) {
			divider--;
		}

		unsigned long int other_divider = (unsigned long int)(a/divider);
		
		if(divider != 1 && other_divider != 1) {
			facteurs(divider);
			facteurs(other_divider);
		}
		if(divider == 1 && other_divider != 1) {
			printf("%lu\n", other_divider);
		}
		if(divider != 1 && other_divider == 1) {
			printf("%lu\n", divider);
		}	
	}
}

int main(int argc, char* argv[])
{
	facteurs_premiers(600851475143);

	return 0;
}

