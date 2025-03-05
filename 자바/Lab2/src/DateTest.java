/*작성자: 임다희(2312282)
 *작성일: 2024-09-19
 *Lab2-5. MyDate 클래스 작성*/

import java.util.Scanner;

class MyDate {

	private int year, month, day;
	//필드 선언(int 형태로 연도, 달, 날짜를 나타냄)
	
	public MyDate(int year, int month, int day) {
		this.year=year;
		this.month=month;
		this.day=day;
	}
	//MyDate의 생성자 정의
	
	public void printDate1() {
		System.out.println(year+"."+month+"."+day);
	}
	//MyDate의 필드값 정보를 문자열로 출력하는 printDate1 메소드. 
	//연도, 달, 날짜 순으로 출력한다. 
	
	public void printDate2() {
		
		String months[]= {"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"};
		System.out.println(months[month-1]+" "+day+","+year);
	}	
	//MyDate의 필드값 정보를 문자열로 출력하는 printDate2 메소드. 
	//달, 날짜, 연도 순으로 출력한다. 
	//숫자로 표현한 달에 해당하는 문자열 달을 출력하기 위해 달 문자열을 원소로 가진 배열 months를 만든다. 
	//months[month-1]로 올바른 문자열에 접근해 출력한다. 	
}

//DateTest 클래스.
public class DateTest {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("연도: ");
		int y=sc.nextInt();
		System.out.print("월: ");
		int m=sc.nextInt();
		System.out.print("일: ");
		int d=sc.nextInt();	
		//사용자에게 연도, 월, 일에 대한 정보를 입력받는다. 
		
		MyDate date=new MyDate(y,m,d);
		//Mydate 클래스의 객체 date를 생성한다. (사용자에게 입력받은 정보 기반)
		date.printDate1();	
		date.printDate2();
		//printDate1,printDate2 메소드를 각각 실행한다. 
	}
}
