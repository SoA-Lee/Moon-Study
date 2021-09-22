#include <stdio.h>

int main(void) {

	int T;
	int n = 0, sum[100] = { 0 }, a[100] = { 0 };
	
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) scanf("%d", &a[i]);
	
	for (int i = 1; i<=T; i++) {
		for (int j = 1; j <= a[i]; j++) {
			if (j % 2 != 0) sum[n] += j;
		}
		printf("%d\n", sum[n]);
		n++;
	}
}
