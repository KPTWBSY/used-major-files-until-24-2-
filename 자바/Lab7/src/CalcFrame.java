/*작성자: 임다희(2312282)
 *작성일: 2024-11-03
 *Lab7-4 CalcFrame 클래스*/

import java.awt.*;
import java.awt.event.*;
import javax.swing.*; //GUI 구성에 필요한 패키지를 import한다. 

public class CalcFrame extends JFrame {

	private JButton equals; 
	private JTextField num1;
	private JTextField num2;
	private JTextField result;
	//이벤트 처리에 필요한 JButton과 JTextField들을 정의한다.

	class MyListener implements ActionListener { //액션 리스너 인터페이스를 구현하는 MyListener 클래스. 
		public void actionPerformed(ActionEvent e) {
			//ActionEvent의 발생을 확인하면 실행할 내용.
			int num_1 = Integer.parseInt(num1.getText());
			int num_2 = Integer.parseInt(num2.getText());
			//곱셈 연산을 진행할 수를 나타내는 2개의 JTextField에서 입력받은 값을 각각 받아온다.  
			
			result.setText(Integer.toString(num_1 * num_2));
			//결과값을 나타내는 텍스트 필드에 실제 연산된 값을 표시한다.
		}
	}

	public CalcFrame() {
		setSize(400, 120);
		setTitle("계산기"); //프레임의 크기와 제목을 지정한다.

		num1 = new JTextField(5);
		num2 = new JTextField(5);
		result = new JTextField(10); //텍스트 필드의 크기(글자수)를 지정한다. 

		JLabel x = new JLabel("X"); //곱셈 기호를 나타내는 라벨을 생성한다. 

		equals = new JButton("="); //버튼을 생성한다. 
		equals.addActionListener(new MyListener()); //버튼에 이벤트 리스너를 붙인다. 

		add(num1);
		add(x);
		add(num2);
		add(equals);
		add(result);
		//프레임에 텍스트필드, 라벨, 버튼들을 알맞은 순서로 배치한다. 

		setLayout(new FlowLayout(FlowLayout.CENTER));
		//배치 관리자를 통해 가운데 정렬된 FlowLayout 형태로 요소들을 배치한다. 

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new CalcFrame();
	}

}
