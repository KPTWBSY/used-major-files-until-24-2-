/*작성자: 임다희(2312282)
 *작성일: 2024-09-26
 *Lab3-1.BankAccount 클래스 작성*/

import java.util.Scanner;

class BankAccount { //BankAccount 클래스 작성
	private int balance; //필드 선언 

	BankAccount(int balance) {
		this.balance = balance;
	} //BankAccount 클래스의 생성자 정의

	//각 필드에 대한 접근자, 생성자 메소드 작성
	public int getBalance() {
		return balance;
	}

	public void setBalance(int balance) {
		this.balance = balance;
	}

	//입금 메소드 생성. 
	public int deposit(int amount) {
		//매개변수로 들어온 입금 금액 amount가 양수일 때 처리되도록 한다. 
		if (amount > 0) {
			balance += amount;
		}
		return balance;
	}

	//출금 메소드 생성.
	public int withdraw(int amount) {
		//매개변수로 들어온 출금 금액 amount가 현재 잔액보다 클 때 처리되도록 한다. 
		if (amount <= balance) {
			balance -= amount;
		}
		return balance;
	}
	
	//toString 메소드. 필드 값 정보를 String 값으로 반환한다. 
	public String toString() {
		return String.format("잔액 : %d ", balance);
	}

	//계좌 이체 메소드 생성. 
	//이체할 금액(int 타입), 이체할 다른 계좌(BankAccount)를 매개변수로 받는다.
	public void transfer(int amount, BankAccount otherAccount) {
		if (amount <= this.balance) {
			this.balance -= amount;
			otherAccount.balance += amount;
		} 
		else {
			System.out.println("잔액이 부족합니다. ");
		}
		//이체할 금액이 현재 잔액보다 많으면 이체하지 않도록 처리한다. 
	}
}

//BankAccountTest 클래스. 
public class BankAccountTest {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("계좌 1 잔액 입력: ");
		int a1 = scan.nextInt();
		BankAccount myAccount1 = new BankAccount(a1);
		System.out.print("계좌 2 잔액 입력 ");
		int a2 = scan.nextInt();
		//사용자에게 매개변수(계좌 잔액)을 입력받아 BankAccount 타입 객체를 2개 만든다. 
		
		BankAccount myAccount2 = new BankAccount(a2);
		System.out.println("myAccount1: " + myAccount1);
		System.out.println("myAccount2: " + myAccount2 + "\n");
		//각 계좌 객체의 필드 정보를 출력한다. 

		System.out.print("계좌 1 --> 계좌 2 이체 금액 입력:");
		int t = scan.nextInt();
		myAccount1.transfer(t, myAccount2);
		//사용자에게 이체할 금액을 입력받아 계좌 1에서 2로 transfer 메소드를 이용해 이체한다. 
		System.out.println("transfer 호출 중");
		System.out.println("myAccount1: " + myAccount1);
		System.out.println("myAccount2: " + myAccount2);
		//이체 후 변화된 각 개체의 잔액 정보를 출력한다. 
	}

}
