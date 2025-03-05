/*작성자: 임다희(2312282)
 *작성일: 2024-09-19
 *Lab2-6. DiceTest 클래스 작성*/

import java.lang.Math;

//Dice 클래스
class Dice{
	private int value; //주사위 면 필드값.
	public Dice() {
		value=0;
	} //Dice 클래스의 생성자. 
	
	public void roll() {
		value=(int)(Math.random()*6+1);
	} //1~6 사이의 랜덤한 값을 생성하는 메소드.
	
	public int getValue() {
		return value;
	} //roll을 통해 생성한 값을 반환하는 메소드.
}

//DiceTest 클래스
public class DiceTest {
	public static void main(String[] args) {
		
		Dice dice1=new Dice();
		Dice dice2=new Dice();
		//Dice 클래스의 객체 2개 생성. 
		int count=0;
		//주사위를 굴린 횟수를 세는 변수 count. 초기값은 0
		
		do {
			dice1.roll();
			dice2.roll(); //roll 메소드를 이용해 주사위 2개를 각각 굴린다. 
			System.out.print("주사위 1="+dice1.getValue()+" ");
			System.out.println("주사위 2="+dice2.getValue());
			//주사위를 굴린 실행결과를 getValue 메소드를 통해 받아와 출력한다. 
			
			count++;
			//실행 횟수를 증가시킨다. 
		}
		while((dice1.getValue()!=1)||(dice2.getValue()!=1));
		//주사위 1, 2의 값이 모두 1이 아닐 경우 do 문 안의 내용을 계속 실행한다. 

		System.out.println("(1,1)이 나오는 데 걸린 횟수 ="+count);
	}
}
