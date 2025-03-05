/*작성자: 임다희(2312282)
 *작성일: 2024-11-21
 *Lab 10-2 HashSet 활용 예제*/

import java.util.*;
import java.util.List;
import java.awt.*;
import javax.swing.*;
//자료구조 사용, GUI 및 이벤트 처리를 위한 패키지 import

class Lotto {
	HashSet<Integer> set = new HashSet<Integer>();
	// 중복 없이 로또 번호 숫자 6개를 저장하는 HashSet을 만든다.

	public void setNumbers() {

		set.clear(); //기존에 저장되어있던 로또 번호를 초기화한다. 
		int len = 0; //확정된 로또 번호 개수를 저장하는 변수 len.

		while (len < 6) { //len이 6 미만일 때(뽑힌 로또 번호가 6개 미만일 때) 다음 내용을 실행한다.
			int num = (int) (Math.random() * 45 + 1);
			//1~45의 난수를 생성한다. 
			if (!set.contains(num)) { 
				//set이 방금 생성된 난수를 포함하고 있는지 확인한다.
				//포함하지 않을 경우 난수를 set에 추가하고,
				//len에 1을 더해 로또 번호가 하나 추가되었음을 표시한다. 
				set.add(num); 
				len++;
			} //set이 생성한 난수를 포함할 경우에는 해당 난수가 set에 추가되지 않고, 
			  //뽑힌 로또번호의 개수도 증가하지 않는다. 
		}
	}

	// Iterator, List 사용하고 (",")로 연결해서 로또번호 문자열로 반환?
	public String setStringNumbers() {
		Iterator<Integer> it = set.iterator();
		// 셋의 모든 요소를 방문하기 위해 반복자를 사용한다.
		List<String> numList = new ArrayList();
		//셋에 저장된 Integer 형태의 로또 번호를 String 문자열로 바꾸어 저장하는 리스트를 만든다. 

		while (it.hasNext()) {
			Integer num = it.next();		
			numList.add(Integer.toString(num));
			//셋의 모든 요소를 방문하며 Integer 형태의 원소를 String 문자열로 바꾸어 numList에 추가한다. 
		}
		return ("Lotto [" + numList + "]");
		//numList를 리턴하여 ","로 연결된 하나의 문자열 형태로 로또 번호를 나타낸다. 
	}
}

public class LottoTest extends JFrame {
	JTextField tf; //로또 번호를 표시할 텍스트 필드
	JButton btn; //누르면 로또 번호 추첨이 실행되는 버튼

	public LottoTest() {
		Lotto lotto = new Lotto(); //Lotto 클래스의 객체 lotto를 생성한다. 

		btn = new JButton("로또 번호 생성");
		btn.addActionListener(e -> {
			//버튼이 눌리는 이벤트 e가 발생하면 다음과 같이 실행된다. 
			lotto.setNumbers(); //로또 번호 생성 메소드를 호출한다. 
			tf.setText(lotto.setStringNumbers()); //결과 문자열을 tf에 설정한다. 
		});

		tf = new JTextField(30);

		//각 요소들을 frame에 추가한다. 
		add(btn, "North"); 
		add(tf, "Center");
		pack();

		setVisible(true);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new LottoTest();

	}

}
