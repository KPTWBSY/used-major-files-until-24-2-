/*작성자: 임다희(2312282)
 *작성일: 2024-11-08
 *Lab8-3 MouseDraggingFrame*/

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
//GUI 구성 및 이벤트 처리에 필요한 패키지를 import한다.

public class MouseDraggingFrame extends JFrame{

	public MouseDraggingFrame() {
		setTitle("드래깅동안 YELLOW");
		setSize(400, 200); // 프레임의 크기와 제목을 지정한다.
		
		getContentPane().setBackground(Color.green);
		//ContentPane의 초기 배경색을 초록색으로 지정한다. 
		
		getContentPane().addMouseMotionListener(new MouseAdapter() {
			//ContentPane에 MouseMotionListener를 추가하고 MouseAdapter를 구현한다. 
			public void mouseDragged(MouseEvent e) {
				getContentPane().setBackground(Color.yellow);
				//마우스를 드래그하는 이벤트가 발생할 시 ContentPane의 배경색을 노란색으로 바꾼다.
			}
			public void mouseMoved(MouseEvent e) {
				getContentPane().setBackground(Color.green);
				//마우스를 클릭하지 않고 단순 이동하는 이벤트가 발생할 시
				//ContentPane의 배경색은 초록색으로 지정된다. 
			}
		});
		
		getContentPane().addMouseListener(new MouseAdapter() {
			//ContentPane에 MouseListener를 추가하고 MouseAdapter를 구현한다. 
			public void mousePressed(MouseEvent e) {
				getContentPane().setBackground(Color.yellow);
			}
			//ContentPane 내에서 클릭 이벤트가 발생할 시 배경색을 노란색으로 바꾼다. 
			public void mouseReleased(MouseEvent e) {
				getContentPane().setBackground(Color.green);
			}
			//ContentPane 내에서 클릭 해제 이벤트가 발생할 시 배경색을 다시 초록색으로 바꾼다. 
		});
		
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public static void main(String[] args) {
		new MouseDraggingFrame();
	}

}
