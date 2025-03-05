/*작성자: 임다희(2312282)
 *작성일: 2024-10-08
 *Lab4-5 BuyerTest 클래스*/

import java.util.Scanner;

class Item { //Item 클래스. 
	protected int price; //가격, 이름을 나타내는 필드 값. 
	protected String name;
}

class Food extends Item{ //Item 클래스를 상속받은 Food 클래스. 
	
	Food(String name, int price){//Food의 생성자. 
		super.name=name; //super.부모 필드변수명 을 통해 부모의 필드값을 지정한다. 
		super.price=price;
	}
	@Override //오버라이딩을 통해 필드 정보를 문자열로 출력하는 메소드를 작성한다. 
	public String toString() {
		return "[Food]" + name ;
	}
}

class Book extends Item{ //Item 클래스를 상속받은 Book 클래스. 
	private String author; // Book의 필드 변수. (저자 정보를 나타냄)
	
	Book(String name, int price,String author){ //Book의 생성자. 
		super.name=name; //부모 필드변수(이름, 가격) 지정
		super.price=price;
		this.author=author; //자신의 필드변수 지정
	}

	@Override //오버라이딩을 통해 필드 정보를 문자열로 출력하는 메소드를 작성한다.
	public String toString() {
		return "[Book]" + name + ", 저자: "+ author;
	}
}

class Movie extends Item{ //Item 클래스를 상속받은 Movie 클래스. 
	private String director; // Item의 필드 변수(감독 정보를 나타냄)
	
	Movie(String name, int price, String director){ //Movie의 생성자. 
		super.name=name; //부모 필드변수(이름, 가격) 지정. 
		super.price=price;
		this.director=director; //자신의 필드변수 지정. 
	}
	
	public String toString() { 
		//오버라이딩을 통해 필드 정보를 문자열로 출력하는 메소드를 작성한다.
		return "[Movie]"+name+", 감독: "+director;
	}
}

class Buyer{ //Buyer 클래스. 
	private int money; //현재 가지고 있는 돈을 나타내는 int 타입 필드변수. 
	
	Buyer(int money){ //Buyer 클래스의 생성자. 
		this.money=money;
	}
	
	public void buy(Item t, int n) { //물건의 이름, 수량을 받아 구매하는 buy 메소드. 
		if(money>t.price*n) { //물건의 가격*수량이 현재 보유한 돈보다 적은지 검사. 
			money-=t.price*n; //현재 보유한 돈이 충분할 경우 총 가격만큼을 차감한다. 
			System.out.println(t.toString()+"=>"+n+"개 구매");
			System.out.println("남은 돈: "+money);
			//구매 정보와 남은 돈의 액수를 출력한다. 
		}
		
		else {System.out.println("돈이 부족합니다.");
		//돈이 충분하지 않을 경우 메세지와 남은 돈의 액수를 출력한다. 
			System.out.println("남은 돈: "+money);
		}
	}
}

public class BuyerTest{ //BuyerTest 클래스. 
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		System.out.print("소지금액을 입력하세요: ");
		int money=scan.nextInt(); //사용자에게 현재 소지금액을 입력받는다. 
		Buyer buyer=new Buyer(money); //입력받은 금액을 바탕으로 Buyer 객체 생성. 
		Item[] items=new Item[5]; //Item 형태를 받는 크기 5의 객체 배열을 생성한다. 
		items[0]=new Food("비빔밥", 9000);
		items[1]=new Food("라면", 6000);
		items[2]=new Food("김밥", 5000);
		items[3]=new Book("자바의 정석", 20000, "남궁성");
		items[4]=new Movie("부산행",15000, "연상호");
		
		while(true) { //종료 조건 전까지 반복해서 상품 정보를 보여줌. 
			System.out.println("구입할 물건을 선택하세요.");
			System.out.println("0. [Food] 비빔밥");
			System.out.println("1. [Food] 라면");
			System.out.println("2. [Food] 김밥");
			System.out.println("3. [Book] 자바의 정석, 저자: 남궁성");
			System.out.println("4. [Movie] 부산행, 감독: 연상호");
			System.out.print("선택 : ");
			int choice=scan.nextInt(); //사용자에게 구매할 물건과 수량을 입력받는다. 
			System.out.print("수량 : ");
			int num=scan.nextInt();
			//사용자 입력을 바탕으로 buy 메소드를 실행한다. 
			buyer.buy(items[choice], num);
			
			System.out.print("계속 구매하시겠습니까?(y/n): ");
			String answer=scan.next();
			//물건 구매 후 계속 구매할지 여부를 사용자에게 입력받는다. 
			if (answer.equals("n")) {
				break; //사용자가 n을 입력하면 while문을 탈출해 실행 종료한다. 
			}
		}	
	}
}