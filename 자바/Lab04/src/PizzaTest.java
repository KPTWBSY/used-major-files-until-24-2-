/*작성자: 임다희(2312282)
 *작성일: 2024-10-08
 *Lab4-1 Pizza 클래스 만들기*/

class Circle {//원을 나타내는 클래스.
	protected int radius; //Circle의 필드변수(원의 지름)
	public Circle(int r) {radius=r;} //Circle의 생성자
}

class Pizza extends Circle {//Circle 클래스를 상속받은 Pizza 클래스.
	
	private String type; //피자의 종류를 나타내는 필드변수.
	
	Pizza(String type, int r){//Pizza의 생성자. 
		super(r); //부모 생성자를 호출한다. 
		this.type=type;
	}

	@Override //오버라이딩을 통해 toString 메소드 작성. 
	public String toString() { //필드 변수 정보를 문자열로 반환한다. 
		return ("피자의 종류: " + type + ", 피자의 크기: "+radius);
	}
}

public class PizzaTest { //PizzaTest 클래스. 
	public static void main(String[] args) {
		Pizza obj=new Pizza("Pepperoni",20); //새로운 피자 객체를 생성한다. 
		System.out.println(obj);
	}
}
