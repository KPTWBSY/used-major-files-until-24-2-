/*작성자: 임다희(2312282)
 *작성일: 2024-09-29
 *Lab3-4.Contacts 클래스 작성*/

import java.util.Scanner;

class Contacts {// Contacts 클래스 작성.
	private String name, tel, email;
	private static int count = 0;

	// 필드 변수 및 static 변수.
	Contacts(String name, String tel, String email) {
		this.name = name;
		this.tel = tel;
		this.email = email;
		count++;
	} // Contacts 클래스의 생성자 정의.
		// 객체가 하나 생성될 때마다 static 변수 count가 1씩 증가한다.

	// 각 필드 변수에 대한 접근자, 생성자 메소드 작성
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getTel() {
		return tel;
	}

	public void setTel(String tel) {
		this.tel = tel;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public static void setCount(int count) {
		Contacts.count = count;
	}

	public static int getCount() {
		return count;
	}

	// toString 메소드. 필드 값 정보를 String 값으로 반환한다.
	public String toString() {
		return "Contacts [name=" + name + ", tel=" + tel + ", email=" + email + "]";
	}
}

public class ContactsTest {// ContactsTest 클래스 작성.
	public static void main(String[] args) {
		Contacts[] list;
		list = new Contacts[100]; // Contacts 객체를 저장하는 객체 배열(최대 100개까지 저장 가능)
		Scanner scan = new Scanner(System.in);
		System.out.println("연락처를 입력하시오(종료 -1)");
		while (true) {
			System.out.print("이름과 전화번호, 이메일을 입력하시오:");
			String x = scan.next();
			// 사용자에게 이름 정보를 입력받는다.
			if (x.equals("-1")) {
				break;
			}
			// 사용자의 입력이 -1이 아니라면 계속 진행한다.
			String y = scan.next();
			String z = scan.next();
			// 사용자에게 전화번호, 이메일 정보를 입력받는다.
			list[Contacts.getCount()] = new Contacts(x, y, z);
			// 객체 배열에 사용자가 입력한 정보를 이용해 새로운 Contacts 객체를 추가한다.
		}
		System.out.println("지인들의 수는 " + Contacts.getCount() + "입니다");
		// static 변수에 접근해 Contacts 객체의 총 개수를 출력한다.
		System.out.print("검색할 이름을 입력하시오: ");
		String name = scan.next();
		// 사용자에게 문자열을 입력받아 객체 배열에 대응하는 값이 있는지 검사한다.
		for (int i = 0; i < list.length; i++) {
			if (list[i] != null && name.equals(list[i].getName())) {
				System.out.print(name + "의 전화번호: " + list[i].getTel() + " 이메일: " + list[i].getEmail());
				// 사용자에게 입력받은 값과 배열 내 Contacts 객체의 Name 값이 같다면
				// 해당 객체의 Tel, Email 값을 함께 출력한다.
			}
		}
	}
}
