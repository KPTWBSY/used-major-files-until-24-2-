/*작성자: 임다희(2312282)
 *작성일: 2024-11-08
 *Lab8-1 MouseEventFrame*/

import javax.swing.JPanel;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
//GUI 구성 및 이벤트 처리에 필요한 패키지를 import한다. 

public class MouseEventFrame extends JFrame {

	JLabel text;
	JPanel panel;

	public MouseEventFrame() {

		setSize(400, 200);
		setTitle("마우스 올리기 내리기");
		// 프레임의 크기와 제목을 지정한다.

		text = new JLabel("Love Java");
		// JLabel 컴포넌트 text. 초기 내용은 "Love Java"이다.

		panel = new JPanel();

		text.addMouseListener(new MouseAdapter() {
			// JLabel 컴포넌트에 MouseAdapter를 익명 클래스로 구현해
			// 마우스 이벤트를 받을 수 있도록 한다.

			public void mouseEntered(MouseEvent e) {
				text.setText("사랑해");
			} // 사용자가 JLabel 컴포넌트 text에 마우스를 들어가게 한 경우
				// text의 내용을 "사랑해"로 설정한다.

			public void mouseExited(MouseEvent e) {
				text.setText("Love Java");
				// 사용자가 text에서 마우스를 나가게 할 경우
				// text의 내용을 다시 "Love JAVA"로 설정한다.
			}

		});

		panel.add(text);
		add(panel);
		// text를 패널에 추가하고 패널을 프레임에 추가한다.

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new MouseEventFrame();
	}

}
