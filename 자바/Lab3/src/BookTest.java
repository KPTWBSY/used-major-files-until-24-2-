/*작성자: 임다희(2312282)
 *작성일: 2024-09-29
 *Lab3-5.Book 클래스 작성*/
import java.util.Scanner;
import java.util.ArrayList;

class Book {//Book 클래스 작성

	private String title;
	private int score; //필드 변수 생성. 

	Book(String title, int score) {
		this.title = title;
		this.score = score;
	}//Book Class의 생성자. 

	// 각 필드 변수에 대한 접근자, 생성자 메소드 작성
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public int getScore() {
		return score;
	}
	public void setScore(int score) {
		this.score = score;
	}
	// toString 메소드. 필드 값 정보를 String 값으로 반환한다.
	public String toString() {
		return "Book [title=" + title + ", score=" + score + "]";
	}
}

public class BookTest {//BookTest 클래스 작성

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		ArrayList<Book> list = new ArrayList<Book>();
		//Book 타입의 원소를 저장하는 동적 객체 배열 생성. 

		while (true) {
			System.out.println("==============================");
			System.out.println("1. 책 등록");
			System.out.println("2. 책 검색");
			System.out.println("3. 모든 책 출력");
			System.out.println("4. 종료");
			System.out.println("==============================");
			//메뉴 목록 출력. 사용자가 종료하기 전까지 계속 반복된다. 
			System.out.print("메뉴를 선택하시오: ");
			int menuNum = scan.nextInt();
			//사용자로부터 메뉴 선택을 숫자로 입력받는다. 

			if (menuNum == 1) {//1번(책 등록)을 입력받은 경우
				scan.nextLine();
				System.out.print("책 제목: ");
				String title = scan.nextLine();

				System.out.print("책 평점: ");
				int score = scan.nextInt();

				list.add(new Book(title, score));
				//책 제목과 평점을 입력받아 새로운 Book 객체를 생성하고 객체 배열에 추가한다. 
			}
			else if (menuNum == 2) {//2번(책 검색)을 입력받은 경우
				System.out.print("책 제목: ");
				scan.nextLine();
				String search = scan.nextLine();//사용자로부터 검색할 책의 제목을 입력받는다. 

				for (int i = 0; i < list.size(); i++) {
					if (list.get(i).getTitle().equals(search)) {
						System.out.println(
								"Book [title=" + list.get(i).getTitle() + ", score=" + list.get(i).getScore() + "]");
					}//객체 배열 내 Book 객체가 사용자에게 입력받은 책 제목과 똑같은 Title 값을 가질 경우 title, score값을 함께 출력한다. 
				}
			}
			else if (menuNum == 3) {//3번(모든 책 출력)을 입력받은 경우
				for (int i = 0; i < list.size(); i++) {
					System.out.println(
							"Book [title=" + list.get(i).getTitle() + ", score=" + list.get(i).getScore() + "]");
				}//객체 배열 내에 있는 모든 Book 객체의 title, score 정보를 출력한다. 
			}
			else if (menuNum == 4) {//4번(종료)을 입력받은 경우
				break;//while 루프문에서 빠져나가 전체 과정을 종료한다. 
			}
		}
	}
}
