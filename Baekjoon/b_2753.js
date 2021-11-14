const fs = require('fs');
const input = fs.readFileSync('/dev/stdin');

const yun = input.toString().split(' ').map(value => +value);

if ((yun % 4 === 0 && yun % 100 !== 0) || ( yun % 400 === 0 )) {
 console.log(1);   
} else {
  console.log(0);
}
/*
# python 풀이
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)

# java 풀이
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int year = sc.nextInt();
        sc.close();
        
        if(year%4==0){
			if(year%400==0) System.out.println("1");
			else if(year%100==0) System.out.println("0");
			else System.out.println("1");
		}
		else System.out.println("0");
	}
}

# C++ 풀이
#include <iostream>
using namespace std;
int main(void){
    int a;
    cin>>a;
    if(a % 4 == 0)
        if(a % 100 != 0 || a % 400 == 0)
            cout<<1;
        else
            cout<<0;
    else
        cout << 0;
}

*/
