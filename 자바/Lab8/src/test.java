

import javax.swing.JButton;
import javax.swing.JPanel;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
public class test extends JFrame {
	JButton btn;
	int x = 100, y = 100;
	public test() {
		setTitle("Mouse 이벤트 테스트");
		JPanel panel = new JPanel();
		panel.setLayout(null);
		btn = new JButton("버튼");
		btn.setBounds(x, y, 100, 50);		
		panel.add(btn);
		add(panel);
		
		panel.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e) {
				x = e.getX()-50;
				y = e.getY()-25;
				btn.setLocation(x, y);
				System.out.println("x");
			}
		});
		
		setSize(400, 300);
		setVisible(true);
	}
	public static void main(String[] args) {
		new test();
	}
}


