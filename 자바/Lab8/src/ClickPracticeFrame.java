/*작성자: 임다희(2312282)
 *작성일: 2024-11-08
 *Lab8-2 CilckPracticeFrame*/

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class ClickPracticeFrame extends JFrame{

	private JLabel c; 
	
	public ClickPracticeFrame() {
		setTitle("클릭 연습용 응용프로그램");
		setSize(400, 400);
		
		setLayout(null); //절대 위치로 요소들을 배치하기 위해 배치 관리자를 null로 설정한다. 
		setVisible(true); 
		//ContentPane의 크기를 받아오기 위해 setVisible 설정을 사전에 해준다. 
		
		c=new JLabel("C"); //"C"를 출력하는 JLabel c
		c.setBounds(100,100,20,20); //c의 초기 위치와 크기 설정. 
		c.addMouseListener(new MouseAdapter() {
			//c에 MouseListener를 추가하고 MouseAdapter를 구현한다. 
			public void mouseClicked(MouseEvent e) {
				//컴포넌트 c를 클릭하는 이벤트 e가 발생하면 다음과 같이 실행하도록 한다.  
				int x=(int)(Math.random()*(getContentPane().getWidth()-20+1));
				//c의 새로운 x좌표를 지정한다.
				//ContentPane의 가로 크기에서 c의 가로 크기를 뺀 값에 1을 더하고 
				//이를 Math.random()으로 생성한 0 이상 1 미만의 난수 값과 곱한다. 
				int y=(int)(Math.random()*(getContentPane().getHeight()-20+1));
				//c의 새로운 y좌표를 지정한다.
				//ContentPane의 세로 크기에서 c의 세로 크기를 뺀 값에 1을 더하고 
				//이를 Math.random()으로 생성한 0 이상 1 미만의 난수 값과 곱한다. 
				c.setLocation(x,y);
				//c의 위치를 생성된 가로, 세로 좌표 난수값에 따라 새로 지정한다.  
			}
		});
		
		add(c); //c를 프레임에 추가한다. 
				
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	
	public static void main(String[] args) {
		new ClickPracticeFrame();
	}

}
