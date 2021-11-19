//solution1
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
	public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
		int N = Integer.parseInt(br.readLine());
		br.close();
		int s = 0;
 
		for( int i = 1 ; i <= N ; i++ ) s+=i;
 
		System.out.println(s);
	}
}

// solution2
import java.util.Scanner;

public class Main{
    public static void main(String[] main){
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int h = 0;
        
        for(int i=0;i<=a;i++){
            h = h + i;
        }
        System.out.println(h);
    }
}
/*
# C++
#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    int h = 0;
    for(int i=1;i<=n;i++){
        h = h + i;
    }
    printf("%d", h);
    return 0;
}

# Python
n = int(input());
h = 0;
for i in range(n+1):
    h = h + i;
print(h);
*/
