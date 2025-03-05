/*작성자: 임다희(2312282)
 *작성일: 2024-10-10
 *Lab5-3 DictionaryApp 클래스*/

import java.util.Scanner;

abstract class PairMap { //추상 클래스 PairMap
	protected String keyArray[]; //Key들을 저장하는 배열
	protected String valueArray[]; //value들을 저장하는 배열. 
	abstract String get(String key); //key값으로 value를 검색하는 메소드. 
	abstract void put(String key, String value); //key,value를 쌍으로 저장. 
	abstract String delete(String key); 
	//key값을 가진 아이템을 대응하는 value와 함께 삭제. 
	
	abstract int length(); //현재 저장된 아이템의 개수 리턴. 
}

class Dictionary extends PairMap { //PairMap을 상속받는 클래스 Dictionary.

	private int count = 0; //현재 저장된 아이템의 개수. 
	public Dictionary(int capacity) { //Dictionary의 생성자. 
		keyArray = new String[capacity]; 
		valueArray = new String[capacity];
		//사용자에게 배열의 크기 값을 입력받아 해당 크기의 String 객체 배열을 2개 만든다. 
		//(각각 key값을 저장하는 배열, value값을 저장하는 배열이다)
	}

	public String get(String key) { //get 메소드를 구현한다. 
		for (int i = 0; i < count; i++) { 
			//현재 keyArray 객체 배열 내의 모든 객체들에 대해 key와 값이 일치하는지 확인.  
			if (keyArray[i].equals(key)) {
				return valueArray[i]; 
				//일치하는 경우 해당 key에 대응하는 value 값 반환. 
			}
		}
		return null; //key를 발견하지 못한 경우 null 리턴. 
	}

	void put(String key, String value) { //put 메소드를 구현한다. 
		for (int i = 0; i < count + 1; i++) {
			//현재 keyArray 객체 배열에 저장된 모든 객체들에 대해
			if (key.equals(keyArray[i])) {
				//이미 입력받은 key값과 일치하는 값이 존재하면 
				//대응하는 valueArray의 값을 새로 입력받은 값으로 덮어씌운다. 
				valueArray[i] = value;
				break;
			} else { //그 외의 경우 새로운 key와 value값을 배열의 가장 끝에 추가한다. 
				keyArray[count] = key;
				valueArray[count] = value;
			}
		}

		if (keyArray[count] != null && valueArray[count] != null) {
			//새로운 key와 value 값이 성공적으로 배열의 맨 끝에 추가된 경우
			count++; //count값을 1 증가시켜 현재 저장된 아이템의 개수를 증가시킴. 
		}
	}

	String delete(String key) { //delete 메소드 구현. 
		for (int i = 0; i < count; i++) {
			//현재 keyArray 객체 배열에 저장된 모든 객체에 대해
			if (keyArray[i].equals(key)) {
				//이미 존재하는 key값 중 입력받은 key값과 일치하는 값이 존재할 경우
				String value = valueArray[i]; 

				keyArray[i] = valueArray[i] = null; 
				//해당 위치의 key, value 값 삭제.  

				for (int j = i + 1; j < count; j++) {
					keyArray[j-1] = keyArray[j];
					valueArray[j-1] = valueArray[j];	
				} //삭제한 위치의 뒤에 있는 원소들을 앞으로 한칸씩 이동한다. 

				count--; //저장된 아이템의 개수를 1만큼 줄인다. 
				return value; //삭제된 key에 대응하는 value값을 리턴한다. 
			}
		}
		return null; //key값이 배열에 저장되어 있지 않은 경우 null값을 반환한다. 
	}

	int length() {
		return count; //저장된 아이템의 개수를 리턴한다. 
	}
}

public class DictionaryApp { //DictionaryApp 클래스
	public static void main(String[] args) {

		Dictionary dic = new Dictionary(100); 
		//크기 100의 Dictionary 객체 생성. 

		Scanner sc = new Scanner(System.in);
		boolean run = true; //아래의 while문이 실행되도록 하는 변수. 

		System.out.println("한영 단어 등록 프로그램입니다. ");

		while (run) {
			System.out.println(
					"===================================" + "\n " + "1. 단어 등록" + "\n " + "2. 단어 검색" + "\n " + "3. 단어 삭제"
							+ "\n " + "4. 모든 단어 보기" + "\n " + "5. 종료" + "\n " + "===================================");
			System.out.print("메뉴를 선택하세요>>");
			int choice = sc.nextInt(); //사용자에게 메뉴 선택을 입력받는다. 
 
			switch (choice) { //switch 문을 통해 각 case별로 실행을 달리 함. 
			case 1 -> { //1번 입력을 받은 경우 새로운 한영 단어를 등록. 
				System.out.print("한영 단어를 등록하시오. ex) 과학 science >> ");
				String kor = sc.next();
				String eng = sc.next();
				dic.put(kor, eng);
			}

			case 2 -> { //2번의 경우 단어 입력받아 검색. 
				System.out.print("검색할 단어를 입력하시오. >> ");
				String search = sc.next();
				System.out.println("검색 결과:" + dic.get(search));
			}

			case 3 -> { //3번의 경우 단어 입력받아 삭제. 
				System.out.print("삭제할 단어를 입력하시오. >> ");
				String delete = sc.next();
				System.out.println("삭제 결과:" + dic.delete(delete));
			}

			case 4 -> { //4번의 경우 입력된 모든 단어 보여줌. 
				System.out.println("현재 등록된 모든 단어는 다음과 같습니다.");
				for (int i = 0; i < dic.length(); i++) {
					if (dic.keyArray[i] != null && dic.valueArray[i] != null) {
						System.out.println(dic.keyArray[i] + ": " + dic.valueArray[i]);
					}
				}
			}
			case 5 -> run = false; 
			//5번의 경우 run 변수를 false로 변경하여 while문의 실행 중지.
			}
		}
	}
}