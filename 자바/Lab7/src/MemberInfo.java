/*작성자: 임다희(2312282)
 *작성일: 2024-11-03
 *Lab7-5 Memberinfo*/

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder; //GUI 구성에 필요한 패키지를 import한다. 

public class MemberInfo extends JFrame {

	JLabel[] labels = new JLabel[4]; //JLabel을 저장하는 크기 4의 배열. 
	private JTextField name = new JTextField();
	private JTextField tel = new JTextField();
	private JComboBox box;
	private JButton btn;
	private JTextArea jta = new JTextArea();;
	private JScrollPane jsp;
	//GUI 구성 및 이벤트 처리에 필요한 JTextField, JComboBox, JButton, JTextArea, JScrollPane을 정의한다. 

	class MyListener implements ActionListener { //액션 리스너 인터페이스를 구현하는 MyListener 클래스. 
		public void actionPerformed(ActionEvent e) {
			jta.append(name.getText() + "," + box.getSelectedItem() + "," + tel.getText() + "\n");
		} //ActionEvent가 발생하면 텍스트필드와 콤보박스의 문자열 정보를 받아와 JTextArea에 해당 문자열을 내용으로 추가한다. 
	}

	public MemberInfo() {
		setSize(400, 500);
		setTitle("MemberInfo"); //프레임의 크기와 제목을 지정한다.

		JPanel pan1 = new JPanel(new BorderLayout()); //라벨들과 텍스트필드, 콤보박스를 배치할 패널 pan1.
		JPanel pan2 = new JPanel(new BorderLayout()); //추가 버튼과 JTextArea를 배치할 패널 pan2. 

		JPanel pan3 = new JPanel(new GridLayout(3, 1)); 
		//텍스트필드, 콤보박스를 설명하는 라벨을 배치할 패널 pan3. 3행 1열의 그리드 레이아웃으로 내부 요소를 배치한다. 

		labels[0] = new JLabel("회원 정보 추가"); 
		labels[1] = new JLabel("이름");
		labels[2] = new JLabel("학과");
		labels[3] = new JLabel("연락처");

		for (int i = 1; i < labels.length; i++) {
			pan3.add(labels[i]);
		}
		//패널 4개를 생성하고 그 중 이름, 학과, 연락처 패널은 pan3에 배치한다. 
		pan1.add(pan3, "West"); //pan1에 pan3을 West의 위치로 추가한다. 

		JPanel pan4 = new JPanel(); //회원 정보 추가 라벨을 배치할 패널 pan4
		pan4.add(labels[0]); //pan4에 회원 정보 추가 라벨을 추가한다. 
		pan1.add(pan4, "North"); //pan1에 pan4를 North의 위치로 추가한다. 

		JPanel pan5 = new JPanel(new GridLayout(3, 1, 0, 10)); 
		//텍스트필드와 콤보박스를 배치할 패널 pan5. 3행 1열의 그리드 레이아웃으로 내부 요소를 배치한다.  

		pan5.add(name); //pan5에 이름을 입력받을 텍스트필드를 추가한다. 
		String[] s1 = { "소프트웨어학부", "경영학과", "IT공학과", "문헌정보학과" }; //콤보박스의 메뉴가 될 문자열.
		box = new JComboBox(s1); //문자열을 바탕으로 콤보박스를 생성한다. 
		pan5.add(box); //콤보박스를 pan5에 더한다. 
		pan5.add(tel); //pan5에 연락처를 입력받을 텍스트필드를 추가한다. 

		pan1.add(pan5, "Center"); //pan1에 pan5를 Center의 위치로 추가한다. 

		JPanel pan6 = new JPanel(); //JButton을 배치할 패널 pan6
		btn = new JButton("추가"); //JButton의 내용을 입력하여 새롭게 생성한다. 
		btn.addActionListener(new MyListener()); //버튼에 이벤트 리스너를 추가한다. 
		pan6.add(btn); //pan6에 버튼을 추가한다. 
		pan2.add(pan6, "North"); //pan2에 pan6을 North의 위치로 추가한다. 

		jsp = new JScrollPane(jta, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		//JScrollPane의 내용으로 JTextArea를 추가하고, 수직 방향 스크롤바가 생성되도록 한다. 
		pan2.add(jsp, "Center"); //생성한 스크롤 패널을 pan2에 Center의 위치로 추가한다. 

		pan2.setBorder(new EmptyBorder(5, 5, 5, 5));
		pan3.setBorder(new EmptyBorder(0, 10, 0, 0));
		pan5.setBorder(new EmptyBorder(0, 25, 0, 25));
		//패널들의 외부 간격을 설정한다. 

		setLayout(new GridLayout(2, 1)); //pan1, pan2가 2행 1열의 GridLayout 방식으로 배치되도록 한다. 

		add(pan1);
		add(pan2); //pan1, pan2를 프레임에 추가한다. 

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new MemberInfo();
	}

}
