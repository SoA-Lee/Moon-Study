//1번 풀이_JAVA
public class Main{
    public static void main(String[] args){
        //자바에서 단독으로 백슬래시와 큰 따옴표 쓰기 불가
        // Escape Sequance 사용해야함
        System.out.println("\\    /\\");
		    System.out.println(" )  ( ')");
		    System.out.println("(  /  )");
		    System.out.println(" \\(__)|");  
    }
}

//2번 풀이_JAVA
public class Main{
    public static void main(String[] args){
        
        // StringBuilder 사용하기
        StringBuffer sb = new StringBuffer();
        sb.append("\\    /\\\n");
        sb.append(" )  ( ')\n");
        sb.append("(  /  )\n");
        sb.append(" \\(__)|\n");
        
        System.out.println(sb);
    }
}

//3번 풀이_C
/*
#include <iostream>
using namespace std;
int main(int argc, char const *argv[]) {
    cout << "\\    /\\\n";
    cout << " )  ( ')\n";
    cout << "(  /  )\n";
    cout << " \\(__)|\n";
    return 0;
}
*/

//4번 풀이_JAVASCRIPT
//console.log('\\    /\\\n )  ( \')\n(  /  )\n \\(__)|');
