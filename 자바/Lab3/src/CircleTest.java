/*작성자: 임다희(2312282)
 *작성일: 2024-09-26
 *Lab3-3.Circle 클래스 작성*/
import java.lang.Math;
class Circle {//Circle 클래스 작성
	private int radius;//필드 변수 정의
	public Circle(int d) {
		radius=d;
	}
	//Circle 클래스의 생성자 정의. 
	
	public String toString() {
		return "Circle [radius=" + radius + "]";
	} //toString 메소드. 필드 값 정보를 String 값으로 반환한다.
	
	//radius에 대한 생성자와 접근자. 
	public int getRadius() {
		return radius;
	}
	public void setRadius(int radius) {
		this.radius = radius;
	}
}
public class CircleTest {//CircleTest 클래스 작성. 
	public static void main(String[] args) {
		Circle[] list;
		list=new Circle[3];
		//크기가 3인 Circle 객체 배열을 생성한다. 
		
		for(int i=0; i<list.length; i++) {
			int random=(int)(Math.random()*101);
			//0~100 사이의 난수를 생성한다.  
			list[i]=new Circle(random);
			//랜덤한 매개변수를 받는 Circle 객체를 생성해 배열에 저장한다.  
			System.out.println(list[i]);
		}
	}
}
