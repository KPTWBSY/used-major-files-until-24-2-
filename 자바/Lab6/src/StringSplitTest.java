/*작성자: 임다희(2312282)
 *작성일: 2024-10-20
 *Lab6-3 StringSplitTest 클래스*/

import java.util.Scanner;

public class StringSplitTest {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.print("문자열 입력: ");
		String splitString = sc.nextLine();
		//사용자에게 문자열을 입력받는다. 

		String splitStrings[] = splitString.split(" ");
		//입력받은 문자열을 split 메소드를 이용해 띄어쓰기 단위로 나누어 배열에 저장한다. 
		for (String String : splitStrings) {
			//배열에 있는 문자열을 순서대로 출력한다. 
			System.out.print(String + " / ");
		}

		System.out.println();
		System.out.print("단어 갯수: " + splitStrings.length);
		//문자열의 개수를 출력해 단어의 갯수를 표현한다. 
	}
}
