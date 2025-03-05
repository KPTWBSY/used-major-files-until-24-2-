/*작성자: 임다희(2312282)
 *작성일: 2024-12-05
 *Lab 12-5 CarGame*/
//총 5개의 이미지가 각자의 속도로 움직이도록 설정한 CarGame 코드. 

import javax.swing.*;

public class CarGame extends JFrame {
	class MyThread extends Thread { //스레드 생성을 위해 Thread 클래스를 상속받는다. 
		private JLabel label; //이미지를 나타낼 라벨. 
		private int x, y,speed; //각각 이미지의 x 좌표, y 좌표, 이동 속도를 나타내는 필드. 

		public MyThread(String fname, int x, int y, int speed) { //MyThread의 생성자. 
			this.x = x;
			this.y = y;
			this.speed=speed;  
			label = new JLabel();
			label.setIcon(new ImageIcon(fname));
			//라벨의 아이콘을 fname 입력값으로 받아온 파일명의 이미지로 설정한다. 
			label.setBounds(x, y, 128, 128);
			//라벨의 초기 위치를 설정한다. 
			add(label);
		}

		public void run() { 
			//run() 메소드를 재정의하여 스레드의 작업을 기술한다.  
			for (int i = 0; i < 200; i++) {
				//0.1초마다 label의 x축 위치를 MyThread 객체 생성 시 입력한 속도 값만큼 이동시키는 작업을 수행한다. 
				x += speed;
				label.setBounds(x, y, 128, 128);
				repaint();
				try {
					Thread.sleep(100);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}
	}

	public CarGame() {
		setTitle("CarRace");
		setSize(600, 400);

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(null);

		(new MyThread("car1.gif", 100, 0,10)).start();
		(new MyThread("car2.gif", 100, 50,15)).start();
		(new MyThread("car3.gif", 100, 100,20)).start();
		(new MyThread("car4.gif", 100, 150,25)).start();
		(new MyThread("car5.gif", 100, 200,30)).start();
		//MyThread 객체를 5개 생성한다.
		//각각의 스레드레서 이미지 이동 속도는 10,15,20,25,30 으로 각자의 서로 다른 속도를 가지며 움직이도록 한다. 
		setVisible(true);
	}

	public static void main(String[] args) {
		CarGame t = new CarGame();
	}

}
