import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
 
		int N = in.nextInt();
		in.close();
 
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N - i; j++) {
				System.out.print(" ");
			}
			for (int k = 0; k < i; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}

/*
#include<iostream>
using namespace std;
int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < n - i; j++)
			cout << " ";
		for (int j = 0; j < i; j++)
			cout << "*";
		cout << '\n';
	}
}
*/
