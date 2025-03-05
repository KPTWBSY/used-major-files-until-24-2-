/*작성자: 임다희(2312282)
 *작성일: 2024-09-19
 *Lab2-1. Person 클래스 작성*/

//Person 클래스
class Person {

	private String name, mobile, office, email;
	// 필드 작성(문자열 형태)

	public Person(String n, String m, String o, String e) {
		name = n;
		mobile = m;
		office = o;
		email = e;
	}
	// 생성자 작성(문자열 4개를 변수로 받는다)

	@Override
	public String toString() {

		return String.format("Person [name=%s, mobile=%s, office=%s, email=%s]", name, mobile, office, email);
		// 클래스 필드 정보를 담은 문자열을 출력하는 메소드 toString
	}

	// 각 필드에 대한 접근자와 생성자 메소드.

	public String getName() {
		return name;
	} // name에 대한 접근자.

	public void setName(String name) {
		this.name = name;
	} // name에 대한 생성자.

	public String getMobile() {
		return mobile;
	} // moblie에 대한 접근자.

	public void setMobile(String mobile) {
		this.mobile = mobile;
	} // mobile에 대한 생성자.

	public String getOffice() {
		return office;
	} // office에 대한 접근자.

	public void setOffice(String office) {
		this.office = office;
	} // office에 대한 생성자.

	public String getEmail() {
		return email;
	} // email에 대한 접근자.

	public void setEmail(String email) {
		this.email = email;
	} // email에 대한 생성자.

}

//PersonTest 클래스

public class PersonTest {
	public static void main(String[] args) {
		Person obj = new Person("Kim", "01012345678", "027104567", "a@b.c");
		// Person 클래스의 객체 obj 생성.
		System.out.println(obj);
	}
}