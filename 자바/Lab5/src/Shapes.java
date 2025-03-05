/*작성자: 임다희(2312282)
 *작성일: 2024-10-10
 *Lab5-1 Shapes 클래스*/

interface Shape { //Shape 인터페이스. 
	final double PI = 3.14; //상수 PI 정의. 

	//인터페이스 상속받는 클래스들이 구현해야 할 메소드 정의. 
	void draw(); //도형을 그리는 추상 메소드. 
	double getArea(); //도형의 면적을 리턴하는 추상 메소드. 
	default public void redraw() { //디폴트 메소드. 
		System.out.print("---다시 그립니다.");
		draw();
	}
}

class Circle implements Shape { // Shape 인터페이스를 상속받은 Circle 클래스. 
	
	private int radius; //원의 반지름을 나타내는 필드 변수. 

	Circle(int radius) { //Circle의 생성자. 
		this.radius = radius;
	}

	public double getArea() { //getArea 구현. 
		return PI * radius * radius;
	}

	public void draw() { //draw 구현. 
		System.out.println("반지름이 " + radius + "인 원입니다.");
	}
}

class Oval implements Shape { // Shape 인터페이스를 상속받은 Oval 클래스.

	private int x, y; //타원이 내접하는 사각형의 너비, 높이를 나타내는 변수. 

	Oval(int x, int y) { //Oval의 생성자. 
		this.x = x;
		this.y = y;
	}
	
	//draw, getArea 구현. 
	public double getArea() {
		return PI * x * y / 4;
	}

	public void draw() {
		System.out.println("너비: " + x + ", 높이:" + y + "에 내접하는 타원입니다.");
	}
}

class Rect implements Shape { // Shape 인터페이스를 상속받은 Shape 클래스.

	private int x, y; //사각형의 너비, 높이를 나타내는 필드 변수. 

	Rect(int x, int y) { //Rect의 생성자. 
		this.x = x;
		this.y = y;
	}

	public double getArea() { //getArea, draw 구현. 
		return x * y;
	}

	public void draw() {
		System.out.println("너비: " + x + ", 높이:" + y + "의 사각형입니다.");
	}

}

public class Shapes { //Shapes 클래스. 
	static public void main(String[] args) {
		Shape[] list = new Shape[3]; //Shape 타입의 크기 3 객체 배열 생성. 
		//객체 배열에 Circle, Oval, Rect 객체를 각각 생성해 집어넣는다. 
		list[0] = new Circle(10); 
		list[1] = new Oval(20, 30);
		list[2] = new Rect(10, 40);

		//객체 배열 내의 객체들에 대해 redraw 메소드, getArea 메소드를 실행한다. 
		for (int i = 0; i < list.length; i++)
			list[i].redraw();
		for (int i = 0; i < list.length; i++)
			System.out.println("면적은 " + list[i].getArea());
	}
}
