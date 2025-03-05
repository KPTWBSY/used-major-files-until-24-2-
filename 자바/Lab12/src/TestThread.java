/*작성자: 임다희(2312282)
 *작성일: 2024-12-05
 *Lab 12-3,4 TestThread*/

class MyRunnable implements Runnable{
	//스레드를 생성하기 위해 MyRunnable 클래스에서 Runnable 인터페이스를 구현한다. 
	String myName;
	public MyRunnable(String name) {
		myName=name;
		//스레드 이름
	}
	public void run() {
		for(int i=0; i<=10; i++)
			System.out.print(myName+i+" ");
		//스레드의 기능: 자신의 이름과 함께 숫자 0에서 10까지를 출력합니다.
	}
}

public class TestThread {
	public static void main(String[] args) {
		Thread t1 = new Thread(new MyRunnable("A"));
		Thread t2 = new Thread(new MyRunnable("B"));
		Thread t3 = new Thread(new MyRunnable("C"));
		//Thread t3을 추가해 총 스레드의 개수가 3개가 되도록 한다. (3번 문제)
		t1.start();
		t2.start();
		t3.start();
		
		try {
			t1.join();
			t2.join();
			t3.join();
			//3개의 스레드가 모두 종료되기를 기다린다. (4번 문제)
		} catch (Exception e) {
			System.out.println(e);
		}
		System.out.println("\n프로그램 종료");
		//모든 스레드가 종료되어 출력이 완료되면 프로그램 종료 메세지를 출력한다. (4번 문제)
	}
}