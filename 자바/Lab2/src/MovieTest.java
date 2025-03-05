/*작성자: 임다희(2312282)
 *작성일: 2024-09-19
 *Lab2-3. Movie 클래스 작성*/

import java.util.Scanner;

//Movie 클래스
class Movie {

	//필드 선언 (String, int, double의 형태)
	private String title, director;
	private int year;
	private double rate;
	
	//생성자 정의
	public Movie(String title,double rate,String director,int year) {
		this.title=title;
		this.rate=rate;
		this.director=director;
		this.year=year;
	}
	
	//toString 메소드 작성
	public String toString() {
		return String.format("Movie [title=%s, rating=%.1f, director=%s, year=%d]",title, rate,director ,year);		
	}
		
}

//MovieTest 클래스
public class MovieTest {

	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		System.out.print("제목: ");
		String s=sc.nextLine();
		System.out.print("감독: ");
		String d=sc.nextLine();
		System.out.print("연도: ");
		int year =sc.nextInt();
		System.out.print("평점: ");
		double rating=sc.nextDouble();
		//사용자에게 영화의 제목, 감독, 연도, 평점 정보를 변수를 이용해 받아옴. 
		Movie m=new Movie(s,rating,d,year);
		//Movie 클래스의 객체 m을 생성한다. 
		System.out.println(m);		
		//m의 필드 정보를 나타내는 문자열을 출력한다. 
	}

}
