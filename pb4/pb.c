#include <stdio.h>

int main(int argc, char* argv[])
{
	int i, j, n, max = 0;

	for(i = 1 ; i < 999 ; i++) {
		for(j = i ; j < 999 ; j++) {
			n = i*j;
			
			if(n % 10 == (int)(n/100000)) {
				if((int)((n % 100)/10) == (int)((n % 100000)/10000)) {
					if((int)((n % 1000)/100) == (int)((n % 10000)/1000)) {
						if(max < n) {
							max = n;
						}
					}
				}
			}
		}
	}

	printf("%d\n", max);

	return 0;
}

