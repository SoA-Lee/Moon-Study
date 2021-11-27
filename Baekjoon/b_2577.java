import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
 
		int value = (in.nextInt() * in.nextInt() * in.nextInt());
		String str = Integer.toString(value);
		in.close();
		
		for (int i = 0; i < 10; i++) {
			int count = 0;
			for (int j = 0; j < str.length(); j++) {
				if ((str.charAt(j) - '0') == i) {
					count++;
				}
			}
			System.out.println(count);
		}
		
	}
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
public class Main {
	public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
		int val = Integer.parseInt(br.readLine())*Integer.parseInt(br.readLine())*Integer.parseInt(br.readLine());
		int[] arr = new int[10];
		
		while(val!=0) {
			arr[val%10]++;
			val/=10;
		}
		
		for(int result : arr) {
			System.out.println(result);
		}
	}
}
/*
# C++
#include<iostream> 
using namespace std; 
int main() { 
  int A, B, C; 
  int multiply; 
  int cntArr[10] = { 0, }; 
  cin >> A >> B >> C; 
  multiply = A * B * C; 
  
  while (multiply>0) { 
    cntArr[multiply % 10]++; 
    multiply /= 10; 
    } 
    for (int i=0;i<10;i++) 
    { 
        cout << cntArr[i] << endl; 
    } 
      return 0; 
}


# C
# include<stdio.h>

int main(){
    int a,b,c;
    int arr[10]={0,};
    scanf("%d %d %d", &a, &b, &c);
    int n = a*b*c;
    
    int num;
    while(n>0){
        num = n%10;
        arr[num]++;
        n/=10;
    }
    
    for(int i=0; i<10; i++) {
        printf("%d\n", arr[i]);
    }
    return 0;
}


# python
a = int(input())
b = int(input())
c = int(input())

total = list(str(a*b*c))
for i in range(10):
    print(total.count(str(i)))
*/
