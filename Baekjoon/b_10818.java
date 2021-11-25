// sol.1
import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] arr = new int[N];
        
        for(int i=0;i<N;i++){
            arr[i] = sc.nextInt();
        }
        sc.close();
        Arrays.sort(arr);
        System.out.print(arr[0] + " " + arr[N - 1]);
    }
}

// sol.2
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
		Integer.parseInt(br.readLine());	//첫 줄 N 은 안쓰이므로 입력만 받는다.
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		int max = -1000001;
		int min = 1000001;
		
		while(st.hasMoreTokens()) {
			int val = Integer.parseInt(st.nextToken());
			if(val>max) {
				max = val;
			}
			if(val<min) {
				min = val;
			}
		}
		System.out.println(min + " " + max);
	}
}

/*
# C++ (version2)
#include <iostream>
#include <algorithm>
 
using namespace std;
 
int main(int argc, const char * argv[]) {
 
	ios_base::sync_with_stdio(0);
 
	int N;
	cin >> N;
 
	int array[1000001];
 
	for(int i = 0; i < N; i++) {
		cin >> array[i];
	}
 
	sort(array, array + N);		// 0 ~ N-1 범위 정렬
 
	cout << array[0] << " " << array[N - 1];
 
	return 0;
 
}

# C++ (version1)
#include <iostream>
using namespace std;

int main()
{
   int n;
   int temp;
   int min = 1000000, max = -1000000;
   
   cin >> n;
   
   for(int i = 1; i <= n; i++)
   {
       cin >> temp; 
       if (temp < min)
            min = temp;
       if (temp > max)
            max = temp;
   }
       
   cout << min << " " << max << endl;
}

# Python
cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)
*/
