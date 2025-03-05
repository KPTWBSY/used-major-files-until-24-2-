/*작성자: 임다희(2312282)
 *작성일: 2024-10-08
 *Lab4-2 Magazine 클래스 만들기*/

class MyBook {//Mybook 클래스. 
	
	protected String title, author; //필드 변수 정의. (책의 제목, 저자)
	protected int page; //책의 페이지 수
	protected static int count; //static 변수 정의. (생성된 MyBook타입 객체 개수)
	
	MyBook(String title, int page, String author){
		//MyBook의 생성자. 
		this.title=title;
		this.page=page;
		this.author=author;
		//객체를 하나 생성할 때마다 static 변수의 크기를 1씩 증가시킨다. 
		count++;
	}
	
	//각 필드에 대한 접근자와 생성자. 
	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public int getPage() {
		return page;
	}

	public void setPage(int page) {
		this.page = page;
	}
	//책의 개수에 대한 접근자 메소드. 
	public static int getCount() {
		return count;
	}
}	

public class Magazine extends MyBook {
	//MyBook 클래스를 상속받은 클래스 Magazine. 
	private String date;
	//추가 속성 정보(발매일 정보)
	
	Magazine(String title, int page, String author,String date){
		super(title,page,author); //생성자 내에서 부모 생성자를 호출한다. 
		this.date=date;
	}

	//date 에 대한 생성자와 접근자. 
	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}
	
}

	
