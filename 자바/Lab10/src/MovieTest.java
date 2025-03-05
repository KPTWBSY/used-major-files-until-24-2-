/*작성자: 임다희(2312282)
 *작성일: 2024-11-21
 *Lab 10-3 영화 정보 프로그램*/

import java.util.*; //자료구조 사용을 위한 패키지 import

class Movie { //영화 클래스를 정의한다. 

	private String title, director, genre; //영화의 제목, 감독, 장르를 나타내는 String 필드
	private int year; //영화의 개봉 연도를 나타내는 int 필드

	public Movie(String title, String director, String genre, int year) {
		this.title = title;
		this.director = director;
		this.genre = genre;
		this.year = year;
	} //Movie 클래스의 생성자. 제목, 감독, 장르, 연도 4개의 값을 받아 Movie 객체를 생성한다. 

	@Override
	public String toString() { //Movie 객체의 필드 정볼를 문자열로 출력하는 메소드 toString 
		return "[제목: " + title + "/ 감독: " + director + "/ 장르: " + genre + "/ 개봉년도: " + year + "]";
	}
	
	public String getTitle() { //제목의 getter
		return title;
	}

	public void setTitle(String title) { //제목의 setter
		this.title = title;
	}

	public String getDirector() { //감독의 getter
		return director;
	}

	public void setDirector(String director) { //감독의 setter
		this.director = director;
	}

	public String getGenre() { //장르의 getter
		return genre;
	}

	public void setGenre(String genre) { //장르의 setter
		this.genre = genre;
	}

	public int getYear() { //연도의 getter
		return year;
	}

	public void setYear(int year) { //연도 setter
		this.year = year;
	}
}

public class MovieTest {
	public static void main(String[] args) {
		
		ArrayList<Movie> list = new ArrayList<Movie>();
		//영화 컬렉션을 저장하는 ArrayList 

		Scanner sc = new Scanner(System.in);
		boolean run = true; //while문이 계속 실행되도록 하는 boolean 타입 변수
		while (run) {
			System.out.print(
					"==============영화 정보 관리==============" + "\n" + "1.입력/2.출력/3.검색/4.수정/5.삭제/6.종료" + "\n" + "메뉴입력>>");
			int num = sc.nextInt(); //1~6번까지의 메뉴 옵션 번호를 사용자에게 입력받는다. 

			switch (num) { //입력받은 번호에 따라 다음과 같이 실행한다. 

			case 1 -> { //1번(영화 정보 입력)의 경우
				System.out.print("제목: ");
				sc.nextLine();
				String title = sc.nextLine();
				System.out.print("감독: ");
				String director = sc.nextLine();
				System.out.print("장르: ");
				String genre = sc.nextLine();
				System.out.print("년도: ");
				int year = sc.nextInt();
				//제목, 감독, 장르, 년도 정보를 사용자에게 입력받아 새로운 Movie 객체를 만든다. 
				Movie mov = new Movie(title, director, genre, year);
				list.add(mov); //생성한 Movie 객체를 리스트에 추가한다. 
			}

			case 2 -> { //2번(영화 정보 출력)의 경우
				Iterator<Movie> it = list.iterator();
				// 리스트의 모든 요소를 방문하기 위해 반복자를 사용한다.
				while (it.hasNext()) {
					Movie mov = it.next();
					System.out.println(mov);
					//리스트의 모든 요소를 차례로 방문하며 출력한다.
				}
			}

			case 3 -> { //3번(영화 정보 검색)의 경우
				System.out.print("검색할 제목 입력: ");
				sc.nextLine(); //사용자에게 검색할 영화 제목을 입력받는다. 
				String searchTitle = sc.nextLine();
				Iterator<Movie> it = list.iterator();
				// 리스트의 모든 요소를 방문하기 위해 반복자를 사용한다.
				while (it.hasNext()) {
					Movie mov = it.next();
					if (mov.getTitle().equals(searchTitle)) {
						System.out.println(mov);
					//리스트의 요소 중 제목이 입력받은 제목과 동일한 요소가 있으면
					//헤당 Movie 객체의 정보를 출력한다.
					}
				}
			}

			case 4 -> { //4번(영화 정보 수정)의 경우
				System.out.print("수정할 제목 입력: ");
				sc.nextLine(); //사용자에게 수정할 영화 제목을 입력받는다.
				String Title = sc.nextLine();
				Iterator<Movie> it = list.iterator();
				// 리스트의 모든 요소를 방문하기 위해 반복자를 사용한다.
				while (it.hasNext()) {
					Movie mov = it.next();

					if (mov.getTitle().equals(Title)) {
					//리스트 요소 중 제목이 입력받은 제목과 동일한 요소가 있으면 헤당 Movie 객체의 정보를 출력한다.
						System.out.println(mov);

					//영화의 제목, 감독, 장르, 개봉 연도 값을 다시 입력받는다. 
					//입력받은 특정 필드 값이 Movie 객체가 기존에 가지고 있었던 값과 다를 경우 
					//setter를 통해 해당 필드 값을 재지정한다. 
						System.out.print("제목: ");
						String title = sc.nextLine();
						if (mov.getTitle() != title)
							mov.setTitle(title);

						System.out.print("감독: ");
						String director = sc.nextLine();
						if (mov.getDirector() != director)
							mov.setDirector(director);

						System.out.print("장르: ");
						String genre = sc.nextLine();
						if (mov.getGenre() != genre)
							mov.setGenre(genre);

						System.out.print("년도: ");
						int year = sc.nextInt();
						if (mov.getYear() != year)
							mov.setYear(year);

						System.out.println(mov + "로 수정되었습니다.");
						//수정된 Movie 객체의 필드 정보를 출력한다. 
					}
				}
			}

			case 5 -> { //5번(영화 삭제)의 경우
				System.out.print("삭제할 제목 입력: ");
				sc.nextLine(); //사용자에게 삭제할 영화 제목을 입력받는다.
				String Title = sc.nextLine();
				Iterator<Movie> it = list.iterator();
				// 리스트의 모든 요소를 방문하기 위해 반복자를 사용한다.
				while (it.hasNext()) {
					Movie mov = it.next();
					if (mov.getTitle().equals(Title)) {
					//리스트 요소 중 제목이 입력받은 제목과 동일한 요소가 있으면 헤당 Movie 객체를 리스트에서 삭제한다.
						int i = list.indexOf(mov);
						list.remove(i);
						System.out.println(mov + "이 삭제되었습니다.");
						break; //삭제가 이루어지면 리스트 요소 방문을 멈춘다. 
					//삭제한 Movie 객체 정보를 출력한다.
					}
				}
			}
			case 6 -> { //6번(프로그램 종료)의 경우
				System.out.println("프로그램을 종료합니다."); //프로그램 종료 메세지를 출력한다. 
				run = false; // true일 때 while문이 계속 실행되도록 하는 변수 run 값을 false로 바꾼다. 
			}

			}
		}
	}
}
