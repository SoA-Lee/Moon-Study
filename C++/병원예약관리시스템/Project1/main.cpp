#include <iostream>
#include <string>
using namespace std;

class Console {
public:
	int menu() {
		int num;
		cout << "\n1:예약  2 : 예약 취소  3 : 예약 변경  4 : 예약 확인  5 : 종료>>";
		cin >> num;
		return num;
	}
	int field_menu() {
		int num;
		string department;
		cout << "1:내과, 2:안과, 3:치과 >>";
		cin >> num;
		if (num == 1) {
			department = "내과";
			cout << "\n====="<<department<<" 진료 예약입니다=====\n" << endl;
		}
		else if (num == 2) {
			department = "안과";
			cout << "\n=====" << department << " 진료 예약입니다=====\n" << endl;
		}
		else {
			department = "치과";
			cout << "\n=====" << department << " 진료 예약입니다=====\n" << endl;
		}
		return num;
	}
	int time_menu() {
		int num;
		cout << "1:08시, 2:11시, 3:14ㅑ시, 4:17시>>";
		cin >> num;
		return num;
	}
};

class Time { //시간대 결정
	string name; //name, number를 멤버 변수로 갖는다.
	int number; //시간 번호 저장한다.
public:
	Time() { this->name = " -----"; this->number = -1; } //예약되지 않은 좌석은 ---로 초기화
	void setName(string name) { this->name = name; } //이름 변경
	string getName() { return name; }; //이름 반환
};

class Schedule { 
	Time* time; //time변수 갖는다.
public:
	Schedule() {
		time = new Time[4]; //생성자에서 크기 4인 동적 배열 선언
	}
	void show(int num) { //예약/취소시 해당하는 좌석 상황 보여줌
		if (num == 1)cout << "08시:";
		else if (num == 2)cout << "11시";
		else if (num == 3) cout << "14시:";
		else if (num == 4)cout << "17시:";

		for (int i = 0; i < 4; i++)
			cout << "\t" << time[i].getName();
		cout << endl;
	}
	//시간대 예약 및 취소 시 이름 수정
	void setN(int num, string name) { time[num - 1].setName(name); }
	string getN(int num) { return time[num - 1].getName();} //시간대에 이름 반환
};

class Book {
	Schedule* s; //Schedule변수를 갖는다.
public:
	Book() {
		s = new Schedule[4]; //생성자에서 크가 4인 동적 배열 선언
	}
	void program() { //전체적인 프로그램 구현
		bool exit = true;
		int num;
		Console c;
		int time_num;
		string name;

		while (exit) {
			num = c.menu();
			if (num == 1) {
				num = c.field_menu();
				if (num == 1 || num == 2 || num == 3) {
					num = c.time_menu();
					if (num == 1 || num == 2 || num == 3 || num == 4) {
						cout << "\n \t" << "(1)00분" << "\t" << "(2)15분" << "\t" << "(3)30분" << "\t" << "(4)45분" << endl;
						s[num - 1].show(num);
						cout << "예약 시간 >>";
						cin >> time_num;
						cin.ignore(1); //입력 버퍼 비우기 숫자입력하다 문자 입력하면 반복오류 발생
						cout << "이름 입력 >>";
						getline(cin, name);
						s[num - 1].setN(time_num, name);
					}
					else
						cout << "\n숫자를 잘못 입력하셨습니다." << endl;
				}
			}
			else if (num == 2) {
				num = c.field_menu();
				if (num == 1 || num == 2 || num == 3){
					num = c.time_menu();
					if (num == 1 || num == 2 || num == 3||num==4) {
						cout << "\n \t" << "(1)00분" << "\t" << "(2)15분" << "\t" << "(3)30분" << "\t" << "(4)45분" << endl;
						s[num - 1].show(num);
						cout << "예약 시간 >>"; cin >> time_num;
						cin.ignore(1);
						cout << "이름 입력 >>"; getline(cin, name);
						if (name != s[num - 1].getN(time_num))
							cout << "해당 시간에 예약되어 있는 이름과 일치하지 않습니다." << endl;
						else
							s[num - 1].setN(time_num, " -----");
					}
					else
						cout << "숫자를 잘못 입력하셨습니다." << endl;
				}
			}
			else if (num == 3) {
				num = c.field_menu();
				if (num == 1 || num == 2 || num == 3) {
					num = c.time_menu();
					if (num == 1 || num == 2 || num == 3 || num == 4) {
						cout << "\n \t" << "(1)00분" << "\t" << "(2)15분" << "\t" << "(3)30분" << "\t" << "(4)45분" << endl;
						s[num - 1].show(num);
						cout << "예약 시간 >>"; cin >> time_num;
						cin.ignore(1);
						cout << "이름 입력 >>"; getline(cin, name);
						if (name != s[num - 1].getN(time_num))
							cout << "해당 시간에 예약되어 있는 이름과 일치하지 않습니다." << endl;
						else {
							s[num - 1].setN(time_num, "-----");
							cout << "예약 변경 시간 >>";
							cin >> time_num;
							cin.ignore(1);
							s[num - 1].setN(time_num, name);
						}
					}
					else
						cout << "숫자를 잘못 입력하셨습니다." << endl;
				}
			}
			else if (num == 4) {
				num = c.field_menu();
				if (num == 1 || num == 2 || num == 3) {
					cout << "\n \t" << "(1)00분" << "\t" << "(2)15분" << "\t" << "(3)30분" << "\t" << "(4)45분" << endl;
					for (int i = 1; i <= 4; i++)
						s[i - 1].show(i);
				}
			}
			else if (num == 5) {
				cout << "\n******안녕히 가십시오. 예약을 종료합니다******" << endl;
				break;
			}
			else {
				cout << "숫자를 잘못 입력하셨습니다." << endl;
			}
		}
	}
}; //program멤버함수에서 전체프로그램작성->main함수에 Book변수 동적 생성

	int main() {
		Book* book = new Book();
		cout << "******SWU종합병원에 오신 것을 환영합니다.******" << endl;
		cout << "\n";
		cout << "##한 시간 대에 최대 4명까지 예약 가능합니다##" << endl;
		cout << "##예약 변경은 같은 시간대에서만 가능합니다. 그 외의 경우 취소 후, 새로 예약 부탁드립니다##" << endl;
		book->program();
	}