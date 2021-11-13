// 버퍼 사용하는 방법
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
 
	public static void main(String[] args) throws IOException {
		     
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = br.readLine().split(" ");
		int A = Integer.parseInt(str[0]);
		int B = Integer.parseInt(str[1]);
		
		System.out.println((A>B) ? ">" : ((A<B) ? "<" : "==" )); // 삼항연산자 중복하기
 
	}
}

// 단순히 scanner 사용하는 방법
import java.util.Scanner;
public class Main {
 
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int A = in.nextInt();
		int B = in.nextInt();
		
		in.close();
        
		if(A>B) System.out.println(">");
		else if(A<B) System.out.println("<");
		else System.out.println("==");
	}
}

/*
# C++ 풀이
#include <iostream>
using namespace std;
int main(void) {
	int a, b;
	cin >> a >> b;
	if (a > b)
		cout << ">";
	else if (a < b)
		cout << "<";
	else
		cout << "==";
}
*/
