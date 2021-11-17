let input = require('fs').readFileSync('/dev/stdin').toString();

let num = Number(input[0]);

for (let i = 1; i < 10; i++) {
    console.log(`${num} * ${i} = ${num * i}`);
}
/*
# JAVA 1
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        sc.close();
        
        for(int i=1;i<=9;i++){
            System.out.println(n+" * "+i+" = "+(n*i));
        }
    }
}

# JAVA 2
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
	public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());	
		br.close();
        
		for(int i = 1; i<10;i++) {
			System.out.println(a+" * "+i+" = "+(a*i));
		}
	}
}

# C++
#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    for(int i=1;i<=9;i++)
        printf("%d * %d = %d\n", n,i,n*i);
    return 0;
}

# Python
a = int(input())
for i in range(1,10):
    print(a,'*',i,'=',a*i)
*/
