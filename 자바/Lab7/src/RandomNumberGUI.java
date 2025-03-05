/*작성자: 임다희(2312282)
 *작성일: 2024-11-01
 *Lab7-3 RandomNumberGUI 클래스*/

import java.awt.*;
import javax.swing.*; //GUI 구성에 필요한 패키지를 import한다. 

public class RandomNumberGUI extends JFrame {

	private JLabel[] labels = new JLabel[30]; //JLabel들을 저장하는 크기 30의 배열.
	private int x_frame = 400; //프레임의 가로 크기. 
	private int y_frame = 200; //프레임의 세로 크기. 
	private int x_size = 25; //라벨의 가로 크기. 
	private int y_size = 25; //라벨의 세로 크기. 

	public RandomNumberGUI() {
		setTitle("My Frame");
		setSize(x_frame, y_frame);
		//프레임의 크기와 제목을 지정한다. 
		setLayout(null); //프레임의 배치 관리자를 설정한다. 절대 위치로 요소들을 배치하기 위해 null을 사용한다. 
		setVisible(true); //ContentPane의 크기를 받아오기 위해 setVisible 설정을 사전에 해준다. 

		int x_actualSize = getContentPane().getWidth(); 
		int y_actualSize = getContentPane().getHeight();
		//getContentPane() 을 통해 프레임에서 메뉴바 등의 부가적인 요소를 제외한 ContentPane의 크기를 받아온다. 
		//getWidth(), getHeight()를 통해 ContentPane의 가로, 세로 크기를 변수값에 저장한다. 

		for (int i = 0; i < labels.length; i++) {
			labels[i] = new JLabel(Integer.toString(i));
			add(labels[i]);
			//0~29까지의 정수 문자열을 가진 라벨 30개를 생성해 프레임에 추가한다. 
			labels[i].setBounds((int) (Math.random() * (x_actualSize - x_size+1)),
					(int) (Math.random() * (y_actualSize - y_size+1)), x_size, y_size);
			//setBounds를 통해 각 라벨의 위치와 크기를 설정한다. 
			//라벨의 x좌표 값은 0 이상, ContentPane의 가로 크기에서 라벨의 가로 크기를 뺀 값 이하의 난수이다. 
			//라벨의 y좌표 값은 0 이상, ContentPane의 세로 크기에서 라벨의 세로 크기를 뺀 값 이하의 난수이다.
			//Math.random()을 통해 난수를 생성하고, 
			//ContentPane의 가로 or 세로 크기-라벨의 가로 or 세로 크기 +1 을 곱해 최종적인 값을 정수로 타입캐스팅한다.
			
			labels[i].setForeground(Color.RED); //라벨의 색상을 설정한다. 
		}

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {

		RandomNumberGUI r = new RandomNumberGUI();

	}

}
