import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
		
		int N = in.nextInt();
		int M = in.nextInt();
 
		int[] arr = new int[N];
 
		for (int i = 0; i < N; i++) {
			arr[i] = in.nextInt();
		}
		
		int result = search(arr, N, M);
		System.out.println(result);
	}
 
	
	// 탐색
	static int search(int[] arr, int N, int M) {
		int result = 0;
 
		// 3개를 고르기 때문에 첫번째 카드는 N - 2 까지만 
		for (int i = 0; i < N - 2; i++) {
 
			// 두 번째 카드는 첫 번째 카드 다음부터 N - 1 까지만 
			for (int j = i + 1; j < N - 1; j++) {
 
				// 세 번째 카드는 두 번째 카드 다음부터 N 까지 
				for (int k = j + 1; k < N; k++) {
					
					int temp = arr[i] + arr[j] + arr[k];
					if (M == temp) {	
						return temp;
					}
			
					if(result < temp && temp < M) {
						result = temp;
					}
				}
			}
		}
		return result;
	}
}
/*
# C
#include <stdio.h>

int main(void) {

	int N,M;
	int hap= 0;
	int n[100] = { 0 };
	
	scanf("%d %d", &N,&M);
	for (int i = 0; i <N; i++) scanf("%d", &n[i]);
	
	for (int i = 0; i <N - 2; i++) {
		for (int j = i + 1; j < N -1; j++) {
			for (int k = j + 1; k < N; k++) {
				if(n[i] + n[j] + n[k]<=M&&M-(n[i] + n[j] + n[k])<M-hap)
				hap = n[i] + n[j] + n[k];
				}
			}
		}
	printf("%d", hap);
	}
  
# Python 
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = len(a)
sum = 0
for i in range(0, b - 2):
        for j in range(i + 1, b - 1):
                for k in range(j + 1, b):
                        if a[i] + a[j] + a[k] > m:
                                continue
                        else:
                                sum = max(sum, a[i] + a[j] + a[k])
print(sum)
*/
