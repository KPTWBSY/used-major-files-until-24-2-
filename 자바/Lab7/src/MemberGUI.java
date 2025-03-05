/*작성자: 임다희(2312282)
 *작성일: 2024-11-01
 *Lab7-2 MemberGUI 클래스*/

import java.awt.*;
import javax.swing.*;  //GUI 구성에 필요한 패키지를 import한다. 

public class MemberGUI extends JFrame {

	public MemberGUI() {
		setTitle("회원 정보 등록 화면");
		setSize(400, 300);
		//프레임의 크기와 제목을 지정한다. 

		setLayout(new BorderLayout());
		//프레임의 배치 관리자를 BorderLayout으로 설정한다.

		JPanel p1 = new JPanel();
		JPanel p2 = new JPanel(new GridLayout(4, 1));
		JPanel p3 = new JPanel(new GridLayout(4, 1));
		JPanel p4 = new JPanel();
		//프레임에 설치할 패널 4개를 생성한다. 이 중 두 패널은 내부 요소가 4행 1열의 GridLayout으로 배치되도록 한다. 

		p1.add(new JLabel("회원 등록")); //패널 p1에 회원 등록 라벨을 추가한다.
		
		p2.add(new JLabel("이름"));
		p2.add(new JLabel("패스워드"));
		p2.add(new JLabel("이메일 주소"));
		p2.add(new JLabel("전화번호")); //패널 p2에 라벨 4개를 추가한다. 이는 배치 관리자 설정대로 4행 1열로 배치된다. 

		JTextField t_name = new JTextField(30);
		t_name.setText("홍길동");
		JTextField t_passwd = new JTextField(30);
		JTextField t_email = new JTextField(30);
		t_email.setText("abc@example.com");
		JTextField t_tel = new JTextField(30);
		t_tel.setText("010-1234-5678");
		//새로운 30자 분량의 JTextField 4개를 생성한다. 

		p3.add(t_name);
		p3.add(t_passwd);
		p3.add(t_email);
		p3.add(t_tel);
		//생성한 텍스트 필드를 패널 p3에 추가한다. 이는 배치 관리자 설정대로 4행 1열로 배치된다. 

		p4.add(new JButton("등록하기"));
		p4.add(new JButton("취소"));
		//패널 p4에 등록 버튼과 취소 버튼을 추가한다. 

		add(p1, "North");
		add(p2, "West");
		add(p3, "Center");
		add(p4, "South");
		//패널 p1~p4를 프레임상에 각각 배치한다. 

		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {

		MemberGUI m = new MemberGUI();

	}

}
