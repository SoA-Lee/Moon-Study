import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int[] arr;
		
		int testcase = in.nextInt();
		
		for(int i = 0 ; i < testcase ; i++) {
 
			int N = in.nextInt();	//학생 수 
			arr = new int[N];
			
			double sum = 0;	// 성적 누적 합 변수 
			
			// 성적 입력부분 
			for(int j = 0 ; j < N ; j++) {
				int val = in.nextInt();	// 성적 입력 
				arr[j] = val;
				sum += val;	// 성적 누적 합 
			}		
			double mean = (sum / N) ;
			double count = 0; // 평균 넘는 학생 수 변수 
			
			// 평균 넘는 학생 비율 찾기 
			for(int j = 0 ; j < N ; j++) {
				if(arr[j] > mean) {
					count++;
				}
			}		
			System.out.printf("%.3f%%\n",(count/N)*100);
		}
		in.close();
	}
}
/*
# python
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')
*/
