// Java
import java.util.Scanner;
import java.util.HashSet;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> h = new HashSet<Integer>();
        
        for(int i=0;i<10;i++){
            h.add(sc.nextInt()%42);
        }
        sc.close();
        System.out.print(h.size()); 
    }
}

/*
# C
#include <stdio.h>

int main(void) {
    
    int input, result=0;
    int remain[10];
    
    for(int i=0; i<10; i++) {
        scanf("%d", &input);
        remain[i] = (input % 42);
    }
    
    for(int i=0; i<10; i++) {
        int count=0; 
        for(int j=i+1; j<10; j++) { // 서로 같은 수일 경우
            if(remain[i] == remain[j]) count++;
        }
        if (count == 0) result++; // 같은 수가 없을 경우 
    }
    
   printf("%d", result);
}

# python
arr = []
for i in range(10):
    n = int(input())
    arr.append(n%42)
arr = set(arr)
print(len(arr))
*/
