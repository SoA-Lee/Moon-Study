let input = require('fs').readFileSync('dev/stdin').toString().split(' ');

let Hour = Number(input[0]);  // Hour
let Minute = Number(input[1]);  // Minute

Minute -= 45;

if (Minute < 0) {
    Minute += 60;
    Hour--;

    if (Hour === -1) {
        Hour = 23;
    }
}

console.log(Hour + ' ' + Minute);

/*
# Java
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int H = sc.nextInt();
        int M = sc.nextInt();
        sc.close();
        
        if(M < 45) {
			H--;		// 시(hour) 1 감소
			M= 60 - (45 - M); 	// 분(min) 감소
			if(H < 0) {
				H = 23;
			}
			System.out.println(H + " " + M);
		}
		else {
			System.out.println(H + " " + (M - 45));
		}
    }
}
# C++
# include <iostream>
using namespace std;

int main() {
	int hour, min;
	cin >> hour >> min;

	if (min < 45) {
		if (hour == 0)
			cout << 23 << " " << min + 15 << endl;
		else
			cout << hour - 1 << " " << min + 15 << endl;
	}
	else {
		cout << hour << " " << min - 45 << endl;
	}
}

# Python
h,m = map(int,input().split())

if m<45 :
    if h ==0:
        h=23
        m+=60
    else:
        h-=1
        m+=60
print(h,m-45)
*/
