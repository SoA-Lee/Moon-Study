import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {		
		Scanner in = new Scanner(System.in);
 
		int N = in.nextInt();
		String a = in.next();
		in.close();
		
		int sum = 0;
        
		for(int i = 0; i < N; i++) {
			sum += a.charAt(i)-'0'; //charAt() 은 해당 문자의 아스키코드 값을 반환하므로 반드시 -48 또는 -'0' 을 해주기
		}
		System.out.print(sum);
	}
}

/*
# C++
#include<iostream>
 
using namespace std;
 
int main()
{
    int N;
    int sum = 0;
    char input;
 
    cin >> N;
 
    for (int i = 0; i < N; i++)
    {
        cin >> input;
        sum += (input - 48);
    }
    cout << sum;
}

# python
n = input()

print(sum(map(int,input())))
*/
