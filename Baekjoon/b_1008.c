#include <stdio.h>

int main() {

	double A,B;
  
  // scanf에서의 포맷 문자가 f인지 lf인지 고민해보기
  // 포맷 문자가 f일 경우 : 파라미터 크기 4로 float 처리, 8일 경우 double 처리
  // scanf가 전달 받는 포인터는 void 타입 포인터
  
	scanf("%lf %lf", &A, &B);
	printf("%.9f\n", A/B);

	return 0;

}

/*
public class Main{
  public static void main(String[] args){
  
  Scanner sc = new Scanner(System.in);
  
  System.out.println((double)sc.nextInt() / sc.nextInt());
  }
}
*/
