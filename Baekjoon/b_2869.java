import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
 
public class Main {
 
	public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
		int up = Integer.parseInt(st.nextToken());
		int down = Integer.parseInt(st.nextToken());
		int length = Integer.parseInt(st.nextToken());
 
		int day = (length - down) / (up - down);
		if ((length - down) % (up - down) != 0)
			day++;
 
		System.out.println(day);
	}
}
/*
# C++
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int A,B,V;
    scanf("%d %d %d",&A,&B,&V);
    int day;
    
    if((V-A)%(A-B)==0)
        day= (V-A)/(A-B);
    else
        day= (V-A)/(A-B)+1;
    
    printf("%d\n",day+1);
 
}

# python
import math

A, B, V = map(int, input().split())
crawl = math.ceil((V-B) / (A-B))
print(crawl)
*/
