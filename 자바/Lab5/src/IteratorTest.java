/*작성자: 임다희(2312282)
 *작성일: 2024-10-10
 *Lab5-2 CardDeck 클래스*/

import java.util.Iterator;

class CardDeck implements Iterator {
	//13장의 카드가 저장된 문자열 객체 배열 cards 생성. 
	String[] cards = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" };
	private int position = 0; //현재 위치를 나타내는 변수 선언, 0으로 초기화. 

	public boolean hasNext() { // 반환할 요소가 있으면 true를 반환하는 메소드. 
		return position < cards.length;
		//현재 위치가 카드 배열의 길이보다 작으면 true,
		//그렇지 않으면 카드 배열의 끝에 도달해 다음 반환할 수가 존재하지 않으므로 false 반환. 
	}

	public Object next() { // 반복의 다음 요소를 반환하는 메소드. 
		String currentCard = cards[position]; 
		//문자열 배열로부터 현재 위치의 값을 반환한다. 
		position++; //현재 위치값을 1만큼 증가시킨다. 
		return currentCard;
	}

	public void remove() {
		//이 반복자가 반환한 마지막 요소를 기본 컬렉션에서 제거하는 메소드. 
		//내부 기능은 구현하지 않고 {} 로만 구현되었다. 
	}
}

public class IteratorTest { //IteratorTest 메소드. 
	public static void main(String[] args) {
		CardDeck i = new CardDeck(); //새로운 CardDeck 객체 i를 생성한다. 
		while (i.hasNext()) { //객체 i의 hasNext가 true값을 만환하는 경우
			System.out.println("next()가 반환하는 값:" + i.next());
			//i.next() 메소드로 다음 요소를 반환한다. 
		}
	}
}
