/*작성자: 임다희(2312282)
 *작성일: 2024-10-08
 *Lab4-3 ColorPoint 클래스 만들기*/

class Point { //Point 클래스 작성. 
	private int x,y; //점의 좌표를 나타내는 필드변수. 
	public Point(int x, int y) { //Point의 생성자. 
		this.x=x;
		this.y=y;
	}

	//각 필드에 대한 접근자. 
	public int getX() {return x;}
	public int getY() {return y;}
	public void setXY(int x,int y) {//x,y값을 동시에 지정하는 메소드. 
		this.x=x;
		this.y=y;
	}
}

class ColorPoint extends Point {//Point 클래스를 상속받은 ColorPoint 클래스. 
	
	private String color;//색을 나타내는 문자열 필드 변수. 
	
	ColorPoint(int x, int y, String color){ //ColorPoint의 생성자. 
		super(x, y); //부모 생성자 호출. 
		this.color=color;
	}
	
	public void setColor(String color) {//color에 대한 생성자. 
		this.color=color;
	}

	public String toString() { //필드 변수 정보를 문자열로 반환하는 메소드. 
		return (color + "색의"+"("+getX()+","+getY()+")의 점");
	}
	
}

public class ColorPointTest {//ColorPointTest 메소드. 

	public static void main(String[] args) {
		ColorPoint cp=new ColorPoint(5,5,"YELLOW");
		//(5,5)의 위치값과 노란색의 color값을 가지는 ColorPoint 객체 생성. 
		cp.setXY(10,20); //setXY 메소드(부모의 메소드)를 통해 객체의 위치값 변경. 
		cp.setColor("RED"); //setColor 메소드(자식의 메소드)를 통해 객체 색 변경. 
		System.out.println(cp.toString()+"입니다. "); //변경된 필드값 정보 출력. 
	}
}
