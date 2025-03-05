/*작성자: 임다희(2312282)
 *작성일: 2024-11-08
 *Lab8-5 AutoRepair*/

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
//GUI 구성 및 이벤트 처리에 필요한 패키지를 import한다.

public class AutoRepair extends JFrame {

	JCheckBox[] checkBoxes = new JCheckBox[4]; // JCheckBox 타입을 저장하는 크기 4의 배열 checkBoxes
	int[] prices = new int[4]; // 크기 4의 정수 배열 prices. 각 수리 선택지에 해당하는 가격을 저장한다.
	int total = 0; // 전체 가격 값을 저장하는 변수.

	public AutoRepair() {
		setTitle("CheckBoxDemo");
		setSize(500, 200);
		// 프레임의 크기와 제목을 지정한다.
		setLayout(new BorderLayout()); // 프레임의 배치 관리자를 BorderLayout으로 지정한다.

		JPanel panel1 = new JPanel(new FlowLayout(FlowLayout.CENTER));
		// CheckBox들을 배치할 JPanel panel1. panel1에 배치되는 요소들은 가운데 정렬된 FlowLayout 형식으로 배치된다.
		JPanel panel2 = new JPanel();
		// 전체 가격값을 나타내는 JLable을 배치할 JPanel panel2

		JLabel text = new JLabel("현재까지의 가격은" + total + "입니다.");
		text.setFont(new Font("Serif", Font.BOLD | Font.ITALIC, 25));
		// 현재 전체 가격값을 나타내는 JLabel text. 글씨체의 크기와 스타일을 조절한다.

		checkBoxes[0] = new JCheckBox("엔진 오일 교환");
		checkBoxes[1] = new JCheckBox("자동 변속기 오일 교환");
		checkBoxes[2] = new JCheckBox("에어컨 필터 교환");
		checkBoxes[3] = new JCheckBox("타이어 교환");
		// 서비스 항목을 나타내는 JCheckBox 4개를 만들어 checkBoxes의 원소로 저장한다.

		prices[0] = 45000;
		prices[1] = 80000;
		prices[2] = 30000;
		prices[3] = 100000;
		// 서비스 항목에 해당하는 가격을 prices의 원소로 저장한다.

		for (int i = 0; i < checkBoxes.length; i++) {
			panel1.add(checkBoxes[i]);
		} // panel1에 checkBoxes의 원소들을 차례로 추가한다.

		panel2.add(text); // panel2에 text를 추가한다.

		for (int j = 0; j < checkBoxes.length; j++) {
			// checkBoxes의 모든 원소들에 대해 해당 작업을 똑같이 실행한다.
			final int i = j;
			checkBoxes[j].addItemListener(new ItemListener() {
				// checkBoxes의 j번째 원소에 ItemListener를 추가하고 익명 클래스로 구현한다.
				public void itemStateChanged(ItemEvent e) {
					// 체크박스의 상태가 변하는 이벤트 e가 발생할 경우
					if (e.getStateChange() == 1) { // 체크박스가 체크된 상태로 변화하는 이벤트일 경우
						total += prices[i]; // 전체 가격에 체크박스의 서비스 항목에 대응하는 가격을 더한다.
					} else // 체크박스가 체크 해제된 상태로 변화하는 이벤트일 경우
						total -= prices[i]; // 전체 가격에서 체크박스의 서비스 항목에 대응하는 가격을 뺀다.
					text.setText("현재까지의 가격은" + total + "입니다.");
					// text의 내용을 변화된 total값을 반영해 다시 설정한다.
				}
			});
		}

		add(panel1, "North"); // panel1을 프레임의 North 위치에 배치한다.
		add(panel2, "Center"); // panel2를 프레임의 Center 위치에 배치한다.

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new AutoRepair();
	}

}
