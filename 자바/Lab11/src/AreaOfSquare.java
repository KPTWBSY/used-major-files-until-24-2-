/*작성자: 임다희(2312282)
 *작성일: 2024-11-29
 *Lab 11-2 AreaOfSquare*/

interface Square{ //하나의 추상 메서드만을 가지는 함수형 인터페이스 Square
		public int getArea(int side);
		//추상 메서드 getArea. 정수형 매개변수를 받아 정수형의 값을 반환한다. 
}

public class AreaOfSquare {
	public static void main(String[] args) {
		
		Square area = (int x) -> x*x;
		//Square 인터페이스를 람다식으로 구현한다. 
		//area: Square 인터페이스를 람다식으로 구현한 객체.
		//Square 인터페이스의 getArea 메소드가 호출되면 x*x 연산이 실행된다. 
				
		System.out.println("면적 결과: "+area.getArea(10));
		//getArea(10)을 호출해 사각형의 면적 계산을 수행한다. (10*10)
	}
}
