/*작성자: 임다희(2312282)
 *작성일: 2024-10-20
 *Lab6-1 CirlceApp 클래스*/

class Circle {

	private int x, y, radius; //Circle 클래스의 필드 변수.
	//원의 중심 좌표 x,y와 반지름 radius를 나타낸다. 

	Circle(int x, int y, int radius) {
		this.x = x;
		this.y = y;
		this.radius = radius;
		//Circle 클래스의 생성자.
	}

	public boolean equals(Object object) {
		Circle circleObject = (Circle) object;
		if (this.x == circleObject.x && this.y == circleObject.y) {
			return true;
		} else
			return false;
		//Object 타입의 변수를 받아 해당 오브젝트와 자신의 중심를 비교해
		//같은 오브젝트인지 아닌지의 여부를 판단하는 equal 메소드. 
		//Object 클래스의 equals()를 재정의한 메소드이다. 
		//object 타입으로 변수를 받아와 Circle 타입으로 변환한 후 비교 시작한다. 
	}

	@Override
	public String toString() {
		return "Circle(" + x + "," + y + ") 반지름" + radius;
	}
	//toString 메소드를 새로 작성하여 필드 변수 정보를 담은 문자열을 출력한다. 
	//Object 클래스의 toString()을 재정의한 메소드이다. 
}

public class CircleApp {
	public static void main(String[] args) {
		Circle a = new Circle(2, 3, 5); // 중심 (2,3)에 반지름 5인 원
		Circle b = new Circle(2, 3, 30); // 중심 (2,3)에 반지름 30인 원
		System.out.println("원 a : " + a);
		System.out.println("원 b : " + b);
		//Circle a와 b가 서로 같은 원인지 다른 원인지 판별한다. 
		if (a.equals(b))
			System.out.println("같은 원");
		else
			System.out.println("서로 다른 원");
	}
}
