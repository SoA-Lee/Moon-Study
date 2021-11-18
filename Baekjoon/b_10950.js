let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

for (let i = 1; i <= input[0]; i++) {
    let numbers = input[i].split(' ');
    
    console.log(Number(numbers[0]) + Number(numbers[1]));
}
/*
# Java
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        int a,b;
        for(int i=0;i<t;i++){
            a = sc.nextInt();
            b = sc.nextInt();
            System.out.println(a+b);
        }
    }
}

# C++
#include <stdio.h>
int main(){
    int a,b,t;
    scanf("%d", &t);
    
    for (int i=0;i<t;i++){
        scanf("%d %d", &a,&b);
        printf("%d\n", a+b);
    }
    return 0;
}

# Python
t = int(input())

for _ in range(t):  
    a,b = map(int,input().split())
    print(a+b)
*/
