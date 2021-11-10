//JAVA 
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        
        // 기초 연산 알고리즘 사용
        Scanner sc = new Scanner(System.in);
        
        int A = sc.nextInt();
        int B = sc.nextInt();
        
        sc.close();
        
        System.out.println(A+B);
    }
}

/*
# PYTHON
a,b = input().split()
print(int(a)+int(b))


# JAVASCRIPT
const fs = require('fs'); # file system 모듈 불러오기
const inputData = fs.readFileSync(0, 'utf8').toString().split(' '); # 경로 동기화 + 자료형 반환

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

console.log(A+B);

# C
# include <stdio.h>
int main() {
  int a,b;
  scanf("%d %d", &a, &b);
  printf("%d\n", a+b);
  return 0;
}
*/
