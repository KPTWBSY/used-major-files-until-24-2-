/*작성자: 임다희(2312282)
 *작성일: 2024-10-08
 *Lab4-4 학생 만들기*/

import java.util.Scanner;

class Human {//Human 클래스 작성. 
	
	protected String name; //이름, 나이 값을 나타내는 필드 변수. 
	protected int age;
	
	public Human(String name, int age) {//Human의 생성자. 
		this.name=name;
		this.age=age;
	}

	//name, age에 대한 생성자와 접근자. 
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}

	@Override //오버라이딩을 통해 필드 변수값을 문자열로 반환하는 메소드 작성. 
	public String toString() {
		return "이름: " + name + ", 나이: " + age;
	}
}

class Student extends Human { //Human 클래스를 상속받은 Student 클래스. 
	
	private String major; //전공, 학번 값을 나타내는 필드 변수. 
	private int sID;
	
	public Student(String name, int age, String major, int sID) {
		//Student의 생성자. 
		super(name,age); //부모의 생성자를 호출한다. 
		this.major=major;
		this.sID=sID;
	}

	//전공 필드에 대한 접근자와 생성자. 
	public String getMajor() { 
		return major;
	}
	public void setMajor(String major) {
		this.major = major;
	}

	@Override
	public String toString() { 
		//오버라이딩을 통해 필드 변수값을 문자열로 반환하는 메소드 작성. 
		//super.toString()을 통해 부모의 toString 메소드를 호출해 연결한다. 
		return ("[학생 정보]"+super.toString()+", 전공:" + major + ", 학번:"+sID+"]");
	}
}

public class StudentTest { //StudentTest 클래스 작성. 
	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		//크기 3의 Human 객체와 Student 객체 배열 생성. 
		Human[] Humans=new Human[3];
		Student[] Students=new Student[3];
		
		//사용자로부터 이름과 나이를 입력받아 3명의 Human 객체를 생성한다. 
		for(int i=0; i<Humans.length; i++) {
			int index=i+1;
			System.out.print("["+index+"] Human 입력:");
			Humans[i]=new Human(sc.next(), sc.nextInt());
		}
		//사용자로부터 이름과 나이, 전공, 학번을 입력받아 3명의 Student 객체를 생성한다. 
		for(int i=0; i<Students.length; i++) {
			int index=i+1;
			System.out.print("["+index+"] Student 입력:");
			Students[i]=new Student(sc.next(), sc.nextInt(), sc.next(), sc.nextInt());
		}
		
		//각 객체참조변수 이름으로 객체 정보를 나타내는 출력문을 출력한다. 
		for(int i=0; i<Humans.length; i++) {
			System.out.println(Humans[i]);
		}
		for(int i=0; i<Students.length; i++) {
			System.out.println(Students[i]);
		}
	}
}
