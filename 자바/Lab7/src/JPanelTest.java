/*작성자: 임다희(2312282)
 *작성일: 2024-11-01
 *Lab7-1 JPanelTest 클래스*/

import java.awt.*;
import javax.swing.*; //GUI 구성에 필요한 패키지를 import한다. 

public class JPanelTest extends JFrame {

	private JPanel[] panels = new JPanel[8];
	private JLabel[] labels = new JLabel[4];
	//JPanel과 JLabel을 저장하는 배열을 생성한다.

	public JPanelTest() {
		setSize(600, 200);
		setTitle("JPanel Test");
		//프레임의 크기와 제목을 지정한다. 

		labels[0] = new JLabel("Red");
		labels[1] = new JLabel("Yellow");
		labels[2] = new JLabel("Green");
		labels[3] = new JLabel("Blue");
		//4개의 라벨을 생성해 JLabel 배열에 저장한다. 

		for (int i = 0; i < panels.length; i++) {
			panels[i] = new JPanel(new BorderLayout());
		}
		//배경색 생성을 위한 4개의 패널, 라벨과 색깔 패널을 함께 붙일 4개의 바탕 패널을 만든다. (총 8개)
		//바탕 패널에는 색깔 패널과 라벨이 BorderLayout 방식으로 배치된다. 

		panels[4].setBackground(Color.red);
		panels[5].setBackground(Color.yellow);
		panels[6].setBackground(Color.green);
		panels[7].setBackground(Color.blue);
		//색깔 패널의 배경색을 설정한다. 

		setLayout(new GridLayout(1, 4, 10, 0));
		//레이아웃을 설정한다. 1행 4열의 그리드 레이아웃을 설정하고 x축 방향으로 요소 간 여백을 준다. 
		
		for (int i = 0; i < panels.length / 2; i++) {
			panels[i].add(labels[i], "North");
			panels[i].add(panels[i + 4], "Center");
		}
		//색깔 패널과 해당 색을 나타내는 라벨을 하나의 패널에 함께 설치한다. 
		//색깔 패널은 배경 패널의 Center에, 라벨은 North 위치에 설치되도록
		//각각의 배열에서 for문읉 통해 꺼내어 배치한다. 

		for (int i = 0; i < panels.length / 2; i++) {
			add(panels[i]);
		}
		//배경 패널을 프레임에 설치한다. 

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new JPanelTest();

	}

}
