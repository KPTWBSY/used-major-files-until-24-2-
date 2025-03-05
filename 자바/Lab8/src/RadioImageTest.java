/*작성자: 임다희(2312282)
 *작성일: 2024-11-09
 *Lab8-6 RadioImageTest*/

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.border.EmptyBorder;
//GUI 구성 및 이벤트 처리에 필요한 패키지를 import한다.

public class RadioImageTest extends JFrame {

	JRadioButton[] buttons = new JRadioButton[5]; // JRadioButton 타입을 저장하는 크기 5의 배열 buttons

	public RadioImageTest() {
		setTitle("RadioButtonDemo");
		setSize(550, 400); // 프레임의 크기와 제목을 지정한다.
		setLayout(new BorderLayout()); // 프레임의 배치 관리자를 BorderLayout으로 지정한다.
		String[] animals = { "bird", "cat", "dog", "rabbit", "pig" };
		// 불러올 사진 파일의 이름을 나타내는 문자열들을 저장하는 배열 animals.

		buttons[0] = new JRadioButton(animals[0]);
		buttons[1] = new JRadioButton(animals[1]);
		buttons[2] = new JRadioButton(animals[2]);
		buttons[3] = new JRadioButton(animals[3]);
		buttons[4] = new JRadioButton(animals[4]);
		// animals의 각 문자열을 내용으로 가지는 JRadioButton 5개를 생성해 buttons 배열에 저장한다.

		ButtonGroup group = new ButtonGroup(); // 생성한 JRadioButton을 하나로 묶을 ButtonGroup group.

		JPanel panel1 = new JPanel(new GridLayout(5, 1, 0, 10));
		// JRadioButton들을 배치할 JPanel. 5행 1열의 GridLayout로 배치하며, 요소 간의 y축 간격을 10으로 지정한다.
		JLabel label = new JLabel(); // 사진 파일을 불러와 ImageIcon으로 붙일 JLabel 생성.

		for (int i = 0; i < buttons.length; i++) {
			// buttons 배열의 모든 JRadioButton 원소에 대해 다음과 같이 실행한다.
			final int j = i;
			group.add(buttons[j]); // 모든 JRadioButton을 ButtonGroup group에 추가한다.
			panel1.add(buttons[j]); // 모든 JRadioButton을 panel1에 추가한다.
			buttons[j].addActionListener(new ActionListener() {
				// 모든 JRadioButton에 ActionListener를 추가하고 ActionListener를 익명 클래스로 구현한다.
				public void actionPerformed(ActionEvent e) {
					// j번째 JRadioButton에서 액션 이벤트가 발생하면
					ImageIcon icon = new ImageIcon(animals[j] + ".png");
					label.setIcon(icon);
					//animal의 j번째 원소를 파일 이름으로 가지는 사진을 불러와 ImageIcon으로 설정하고,
					//만들어 둔 JLabel label의 아이콘으로 설정한다. 
				}
			});
		}

		add(panel1, "West"); //panel1을 프레임의 West 위치에 배치한다. 
		add(label, "Center"); //label을 프레임의 Center 위치에 배치한다.

		panel1.setBorder(new EmptyBorder(0, 20, 0, 20));
		//panel1의 외부 간격을 지정한다. 

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new RadioImageTest();
	}

}
