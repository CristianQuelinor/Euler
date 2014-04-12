#include <stdio.h>

int main(int argc, char* argv[])
{
	int premiers[10001];
	premiers[0] = 2;
	premiers[1] = 3;
	int cursor = 1, test, prime = 1, tmp, i;

	while(cursor < 10000) {
		tmp = cursor;
		
		test = premiers[cursor];
		
		while(tmp == cursor) {
			prime = 1;
			test += 2;

			for(i = 0 ; i <= cursor ; i++) {
				if(test % premiers[i] == 0) {
					prime = 0;
					break;
				}
			}

			if(prime == 1) {
				cursor++;
				premiers[cursor] = test;
			}
		}
	}

	printf("%d\n", premiers[10000]);

	return 0;
}

