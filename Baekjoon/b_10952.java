import java.util.Scanner;
 
public class Main {
	public static void main(String args[]){
		
		Scanner in=new Scanner(System.in);
				
		while(true){
		
			int A=in.nextInt();
			int B=in.nextInt();
		
			if(A==0 && B==0){
				in.close();
				break;
			}
			System.out.println(A+B);
		}
	}
}

/*
# C++
#include <iostream>
using namespace std;
int main(void){
    int a, b;
    
    while(1){
        cin>>a>>b;
        if(a!=0 || b!=0)
            cout<<a+b<<endl;
        else
            break;
    }
}

# Python
while(True):
    A, B = list(map(int, input().split()))
    if(A == 0 and B == 0):
        break
    else:
        print(A + B)
*/
