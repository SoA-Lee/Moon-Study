import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
 
		int N = in.nextInt();
		in.close();
        
		int cnt = 0;
		int copy = N;
        
		while (true) {
			N = ((N % 10) * 10) + (((N / 10) + (N % 10)) % 10);
			cnt++;
 
			if (copy == N) {
				break;
			}
		}
		System.out.println(cnt);
	}
}
 
/*
# C++
#include <iostream>
 
using namespace std;
 
int main(int argc, const char *argv[]) {
 
	int init, N;
	int count = 0;
	cin >> init;
 
	N = init;
 
	do {
		N = (N % 10) * 10 + ((N / 10) + (N % 10)) % 10;
 
		count++; // 사이클 증가
	} while (init != N);
 
	cout << count;	
	return 0;
}


# Python 
S = int(input())
N = S
count = 0 
while True:
    ten = N//10
    one = N%10
    res = ten + one
    count += 1
    N = int(str(N%10)+str(res%10))
 
    if (S==N):
        break
print(count)
*/
