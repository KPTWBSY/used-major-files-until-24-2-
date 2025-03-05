/*작성자: 임다희(2312282)
 *작성일: 2024-11-08
 *Lab8-4 MoveStringFrame*/

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
//GUI 구성 및 이벤트 처리에 필요한 패키지를 import한다. 

public class MoveStringFrame extends JFrame {

	private JLabel text; // 회전시킬 문자열을 내용으로 가지는 JLabel 컴포넌트.
	private int count = 0; // 믄자열 분할의 기준이 되는 정수타입의 변수 count

	public MoveStringFrame() {
		setTitle("Left 키로 문자열 회전");
		setSize(400, 200);
		// 프레임의 크기와 제목을 지정한다.

		JPanel panel = new JPanel();

		String T = "Love Java"; // 회전시킬 문자열의 내용은 Love Java이다.
		text = new JLabel(T);

		text.addMouseListener(new MouseAdapter() {
			// text 컴포넌트에 MouseListener를 추가하고 MouseAdapter를 구현한다.
			public void mouseClicked(MouseEvent e) {
				// text 컴포넌트가 클릭되었을 경우 다음과 같이 실행한다.
				if (count < T.length()) {
					// 변수 count의 크기가 문자열의 길이보다 작을 경우(회전이 완전히 진행되어 원본과 같아진 경우가 아니다)
					count++; // count를 1 증가시킨다.
					text.setText(T.substring(count, T.length()).concat(T.substring(0, count)));
					// text의 내용을 새로 설정한다.
					// 문자열 T의 count번째 문자부터 마지막 번째 문자(T.length()-1번째)까지로 이루어진 substring,
					// 0번째 문자부터 count-1번째 문자까지로 이루어진 substring을 concat으로 합친다.
					// 이 문자열을 text의 새로운 내용으로 설정해 실행 이전보다 한 문자만큼 왼쪽으로 밀린 문자열을 표시하도록 한다.
				}

				else { // 회전이 완전히 진행되어 원본과 같아진 경우(count==T.length())
					count = 1; // count를 1로 설정한다.
					text.setText(T.substring(count, T.length()).concat(T.substring(0, count)));
					// 앞의 방법과 똑같이 왼쪽으로 한 문자만큼 민 문자열을 출력한다.
					// count가 다시 T.length() 값과 같아질 때까지 앞의 if문 과정이 반복된다.
				}
			}
		});

		panel.add(text);
		add(panel);

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new MoveStringFrame();
	}

}
