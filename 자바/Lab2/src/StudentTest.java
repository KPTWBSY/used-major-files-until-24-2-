/*작성자: 임다희(2312282)
 *작성일: 2024-09-19
 *Lab2-4. Student 클래스 작성*/

import java.util.Scanner;
//Student 클래스
class Student {
	
	private String name,id;
	private int age;
	//필드 선언 
	
	public Student(String name, String id,int age) {
		this.name=name;
		this.id=id;
		this.age=age;
	}
	//Student 클래스의 생성자 정의
	
	//각 필드에 대한 접근자, 생성자 메소드 작성
	public String getName() {
		return name;
	} //name에 대한 접근자

	public void setName(String name) {
		this.name = name;
	} //name에 대한 생성자

	public String getId() {
		return id;
	} //id에 대한 접근자

	public void setId(String id) {
		this.id = id;
	} //id에 대한 생성자

	public int getAge() {
		return age;
	} //age에 대한 접근자

	public void setAge(int age) {
		this.age = age;
	} //age에 대한 생성자
	
	public String toString() {
		return String.format("Student [이름=%s, 학번=%s, 나이=%d]",name,id,age);		
	} //Student 클래스의 필드값 정보를 문자열로 출력하는 toString 메소드. 
}
//StudentTest 클래스
public class StudentTest {
	public static void main(String[] args) {		
		Scanner sc=new Scanner(System.in);
		System.out.print("학생의 이름: ");
		String name=sc.next();
		System.out.print("학생의 학번: ");
		String id=sc.next();
		System.out.print("학생의 나이: ");
		int age=sc.nextInt();
		//사용자에게 이름, 학번, 나이 정보를 입력받아 변수에 해당 정보 저장
		
		Student s1=new Student(name,id,age);
		//Student 클래스의 객체 s1 생성(사용자에게 입력받은 정보 바탕)
		System.out.println(s1);	
		//s1의 필드값 정보를 문자열로 출력.
	}
}
