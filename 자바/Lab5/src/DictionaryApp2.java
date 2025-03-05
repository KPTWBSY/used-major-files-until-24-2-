/*작성자: 임다희(2312282)
 *작성일: 2024-10-10
 *Lab5-3 DictionaryApp 클래스*/

/*import java.util.Scanner;

abstract class PairMap {
	protected String keyArray[];
	protected String valueArray[];

	abstract String get(String key);

	abstract void put(String key, String value);

	abstract String delete(String key);

	abstract int length();
}

class Dictionary extends PairMap {

	private int count = 0;

	public Dictionary(int capacity) {
		keyArray = new String[capacity];
		valueArray = new String[capacity];
	}

	public String get(String key) {
		for (int i = 0; i < count; i++) {
			if (keyArray[i].equals(key)) {
				return valueArray[i];
			}
		}
		return null;
	}

	void put(String key, String value) {

		for (int i = 0; i < count + 1; i++) {
			if (key.equals(keyArray[i])) {
				valueArray[i] = value;
				break;
			} else {
				keyArray[count] = key;
				valueArray[count] = value;
			}
		}

		if (keyArray[count] != null && valueArray[count] != null) {
			count++;
		}
	}

	String delete(String key) {
		for (int i = 0; i < count; i++) {
			if (keyArray[i].equals(key)) {
				String value = valueArray[i];

				keyArray[i] = valueArray[i] = null;

				for (int j = i + 1; j < count; j++) {
					if (j != count - 1) {
						keyArray[j] = keyArray[j - 1];
						valueArray[j] = valueArray[j - 1];
					}

					keyArray[count - 1] = valueArray[count - 1] = null;
				}

				count--;
				return value;

			}
		}
		return null;
	}

	int length() {
		return count;
	}
}

public class DictionaryApp2 {

	public static void main(String[] args) {

		Dictionary dic = new Dictionary(3);

		Scanner sc = new Scanner(System.in);
		boolean run = true;

		System.out.println("한영 단어 등록 프로그램입니다. ");

		while (run) {
			System.out.println(
					"===================================" + "\n " + "1. 단어 등록" + "\n " + "2. 단어 검색" + "\n " + "3. 단어 삭제"
							+ "\n " + "4. 모든 단어 보기" + "\n " + "5. 종료" + "\n " + "===================================");
			System.out.print("메뉴를 선택하세요>>");
			int choice = sc.nextInt();

			switch (choice) {
			case 1 -> {
				System.out.print("한영 단어를 등록하시오. ex) 과학 science >> ");
				String kor = sc.next();
				String eng = sc.next();
				dic.put(kor, eng);
			}

			case 2 -> {
				System.out.print("검색할 단어를 입력하시오. >> ");
				String search = sc.next();
				System.out.println("검색 결과:" + dic.get(search));
			}

			case 3 -> {
				System.out.print("삭제할 단어를 입력하시오. >> ");
				String delete = sc.next();
				System.out.println("삭제 결과:" + dic.delete(delete));
			}

			case 4 -> {
				System.out.println("현재 등록된 모든 단어는 다음과 같습니다.");
				for (int i = 0; i < dic.length(); i++) {

					if (dic.keyArray[i] != null && dic.valueArray[i] != null) {
						System.out.println(dic.keyArray[i] + ": " + dic.valueArray[i]);
					}
				}
			}

			case 5 -> run = false;
			}

		}
	}
}*/

/*
 * 새로 알게된 것 while문을 스위치문이랑 같이 쓰면서 스위치문 안에 while문 탈출조건을 넣고 싶으면 while문 실행 상태를 나타내는
 * 변수를 따로 지정하고 스위치문에서 종료 원할때 해당 변수를 false로 바꾸는 방식 등으로 해야함 그냥 break 하면 알다시피 스위치문만
 * 빠져나가지고 while문에서는 못나감
 * 
 * 발전된 스위치 -> 는 break를 생략할 수 있는 스위치문인데 -> 다음에 복수의 실행문이 오면 괄호로 묶어야 함.
 */
