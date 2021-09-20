#include<stdio.h>

int main(void) {

	int a1, a2, a3, b1, b2, b3; //득점 입력
	int sumA, sumB = 0; //총합 초기화

	scanf("%d", &a1);
	scanf("%d", &a2);
	scanf("%d", &a3);
	scanf("%d", &b1);
	scanf("%d", &b2);
	scanf("%d", &b3); //

	sumA = 3 * a1 + 2 * a2 + a3;
	sumB= 3 * b1 + 2 * b2 + b3;

	if (sumA > sumB) printf("A"); //A합이 B합보다 클 경우 A 출력
	else if (sumA < sumB) printf("B"); //반대일 경우 B출력
	else printf("T"); //동점일 경우 T출력

	return 0;
}
