// Java 1
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
 
public class Main {
	public static void main(String args[]) throws IOException {
 
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
 
		StringTokenizer st;
		for (int i = 1; i <= a; i++) {
			st = new StringTokenizer(br.readLine()," ");
			System.out.println("Case #" + i + ": " 
			+(Integer.parseInt(st.nextToken())
			+Integer.parseInt(st.nextToken())));
		}
		br.close();
	}
 
}

// Java 2
import java.util.Scanner;
 
public class Main {
	public static void main(String args[]) {
 
		Scanner in = new Scanner(System.in);
 
		int a = in.nextInt();
 
		for (int i = 1; i <= a; i++) {
			int c = in.nextInt();
			int d = in.nextInt();
 
			System.out.println("Case #" + i + ": " + (c + d));
		}
 
		in.close();
	}
}

/*
# c++
#include <iostream>
using namespace std;
int main(void){
    int n, a, b;
    cin>>n;
    for(int i = 0; i < n; i++){
        cin>>a>>b;
        cout <<"Case #" << i+1 << ": "<< a + b <<endl;
    }
}

# python
cases = int(input())

for i in range(cases):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s"%(i+1, ans ))
*/
