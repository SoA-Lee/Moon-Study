import java.io.*;
public class Main {

	public static void main(String[] args) throws IOException {

    // Buffer 사용 시 예외처리 해주기
    // 데이터 재가공해주기
    // 입력데이터들이 string으로 반환됨
    
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < n; i++) {
			String string = br.readLine();
			int a = Integer.parseInt(string.split(" ")[0]);
			int b = Integer.parseInt(string.split(" ")[1]);
			bw.write(a+b+"\n");
		}
		bw.flush();
	}
}
/*
# C++
#include <iostream> 
using namespace std; 
int main(void) { 
    cin.tie(NULL); 
    ios::sync_with_stdio(false); 
    int T; cin >> T; 
    for (int i = 0; i < T; i++) { 
        int A, B; cin >> A >> B; 
        cout << A + B << '\n'; 
    } 
    return 0; 
}

# python
import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
*/
