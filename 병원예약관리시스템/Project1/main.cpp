#include <iostream>
#include <string>
using namespace std;

class Console {
public:
	int menu() {
		int num;
		cout << "\n1:����  2 : ���� ���  3 : ���� ����  4 : ���� Ȯ��  5 : ����>>";
		cin >> num;
		return num;
	}
	int field_menu() {
		int num;
		string department;
		cout << "1:����, 2:�Ȱ�, 3:ġ�� >>";
		cin >> num;
		if (num == 1) {
			department = "����";
			cout << "\n====="<<department<<" ���� �����Դϴ�=====\n" << endl;
		}
		else if (num == 2) {
			department = "�Ȱ�";
			cout << "\n=====" << department << " ���� �����Դϴ�=====\n" << endl;
		}
		else {
			department = "ġ��";
			cout << "\n=====" << department << " ���� �����Դϴ�=====\n" << endl;
		}
		return num;
	}
	int time_menu() {
		int num;
		cout << "1:08��, 2:11��, 3:14����, 4:17��>>";
		cin >> num;
		return num;
	}
};

class Time { //�ð��� ����
	string name; //name, number�� ��� ������ ���´�.
	int number; //�ð� ��ȣ �����Ѵ�.
public:
	Time() { this->name = " -----"; this->number = -1; } //������� ���� �¼��� ---�� �ʱ�ȭ
	void setName(string name) { this->name = name; } //�̸� ����
	string getName() { return name; }; //�̸� ��ȯ
};

class Schedule { 
	Time* time; //time���� ���´�.
public:
	Schedule() {
		time = new Time[4]; //�����ڿ��� ũ�� 4�� ���� �迭 ����
	}
	void show(int num) { //����/��ҽ� �ش��ϴ� �¼� ��Ȳ ������
		if (num == 1)cout << "08��:";
		else if (num == 2)cout << "11��";
		else if (num == 3) cout << "14��:";
		else if (num == 4)cout << "17��:";

		for (int i = 0; i < 4; i++)
			cout << "\t" << time[i].getName();
		cout << endl;
	}
	//�ð��� ���� �� ��� �� �̸� ����
	void setN(int num, string name) { time[num - 1].setName(name); }
	string getN(int num) { return time[num - 1].getName();} //�ð��뿡 �̸� ��ȯ
};

class Book {
	Schedule* s; //Schedule������ ���´�.
public:
	Book() {
		s = new Schedule[4]; //�����ڿ��� ũ�� 4�� ���� �迭 ����
	}
	void program() { //��ü���� ���α׷� ����
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
						cout << "\n \t" << "(1)00��" << "\t" << "(2)15��" << "\t" << "(3)30��" << "\t" << "(4)45��" << endl;
						s[num - 1].show(num);
						cout << "���� �ð� >>";
						cin >> time_num;
						cin.ignore(1); //�Է� ���� ���� �����Է��ϴ� ���� �Է��ϸ� �ݺ����� �߻�
						cout << "�̸� �Է� >>";
						getline(cin, name);
						s[num - 1].setN(time_num, name);
					}
					else
						cout << "\n���ڸ� �߸� �Է��ϼ̽��ϴ�." << endl;
				}
			}
			else if (num == 2) {
				num = c.field_menu();
				if (num == 1 || num == 2 || num == 3){
					num = c.time_menu();
					if (num == 1 || num == 2 || num == 3||num==4) {
						cout << "\n \t" << "(1)00��" << "\t" << "(2)15��" << "\t" << "(3)30��" << "\t" << "(4)45��" << endl;
						s[num - 1].show(num);
						cout << "���� �ð� >>"; cin >> time_num;
						cin.ignore(1);
						cout << "�̸� �Է� >>"; getline(cin, name);
						if (name != s[num - 1].getN(time_num))
							cout << "�ش� �ð��� ����Ǿ� �ִ� �̸��� ��ġ���� �ʽ��ϴ�." << endl;
						else
							s[num - 1].setN(time_num, " -----");
					}
					else
						cout << "���ڸ� �߸� �Է��ϼ̽��ϴ�." << endl;
				}
			}
			else if (num == 3) {
				num = c.field_menu();
				if (num == 1 || num == 2 || num == 3) {
					num = c.time_menu();
					if (num == 1 || num == 2 || num == 3 || num == 4) {
						cout << "\n \t" << "(1)00��" << "\t" << "(2)15��" << "\t" << "(3)30��" << "\t" << "(4)45��" << endl;
						s[num - 1].show(num);
						cout << "���� �ð� >>"; cin >> time_num;
						cin.ignore(1);
						cout << "�̸� �Է� >>"; getline(cin, name);
						if (name != s[num - 1].getN(time_num))
							cout << "�ش� �ð��� ����Ǿ� �ִ� �̸��� ��ġ���� �ʽ��ϴ�." << endl;
						else {
							s[num - 1].setN(time_num, "-----");
							cout << "���� ���� �ð� >>";
							cin >> time_num;
							cin.ignore(1);
							s[num - 1].setN(time_num, name);
						}
					}
					else
						cout << "���ڸ� �߸� �Է��ϼ̽��ϴ�." << endl;
				}
			}
			else if (num == 4) {
				num = c.field_menu();
				if (num == 1 || num == 2 || num == 3) {
					cout << "\n \t" << "(1)00��" << "\t" << "(2)15��" << "\t" << "(3)30��" << "\t" << "(4)45��" << endl;
					for (int i = 1; i <= 4; i++)
						s[i - 1].show(i);
				}
			}
			else if (num == 5) {
				cout << "\n******�ȳ��� ���ʽÿ�. ������ �����մϴ�******" << endl;
				break;
			}
			else {
				cout << "���ڸ� �߸� �Է��ϼ̽��ϴ�." << endl;
			}
		}
	}
}; //program����Լ����� ��ü���α׷��ۼ�->main�Լ��� Book���� ���� ����

	int main() {
		Book* book = new Book();
		cout << "******SWU���պ����� ���� ���� ȯ���մϴ�.******" << endl;
		cout << "\n";
		cout << "##�� �ð� �뿡 �ִ� 4����� ���� �����մϴ�##" << endl;
		cout << "##���� ������ ���� �ð��뿡���� �����մϴ�. �� ���� ��� ��� ��, ���� ���� ��Ź�帳�ϴ�##" << endl;
		book->program();
	}