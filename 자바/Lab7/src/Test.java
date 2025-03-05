

import java.awt.*;
import javax.swing.*;

public class Test extends JFrame {
	
	private JLabel[] labels = new JLabel[30];
	private int x_frame=400;
	private int y_frame=200;
	private int x_width=50;
	private int y_height=50;
	
	public Test() {
		setTitle("My Frame");
		setSize(x_frame, y_frame);
		setLayout(null);
		setVisible(true);
		
		Dimension actualSize=getContentPane().getSize();
		
		JPanel p_test=new JPanel();
		p_test.setBackground(Color.red);
		p_test.setBounds(actualSize.width-x_width,actualSize.height-y_height,x_width,y_height);
		
		add(p_test);

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		
		Test t=new Test();

	}

}
