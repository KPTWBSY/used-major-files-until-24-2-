/*작성자: 임다희(2312282)
 *작성일: 2024-10-20
 *Lab6-5 CharCountTest 클래스*/

import java.util.Arrays;
import java.util.Scanner;

public class CharCountTest {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.print("문장 입력: ");
		String inputString = sc.nextLine();
		//사용자에게 문자열을 입력받는다.

		int[] Chars = new int[26];
		Arrays.fill(Chars, 0);
		//26개의 알파벳 문자의 각 개수를 세는 크기 26의 배열. 모든 인덱스값을 0으로 초기화한다. 

		String[] inputChars = inputString.toUpperCase().split("");
		//입력받은 문자열을 전체 대문자화하고 각 문자 단위로 분리헤 배열에 저장한다. 

		for (int i = 0; i < inputChars.length; i++) {
			try {
				Chars[inputChars[i].charAt(0) - 'A']++;
			} //입력받은 문자열 배열의 각 원소들을 char 형태로 형태 전환하고
			//해당 문자에서 대문자 A를 뺀 숫자에 해당하는 값을 인덱스로 가지는 
			//Chars 배열 값을 1 증가시킨다. 

			catch (ArrayIndexOutOfBoundsException e) {
				System.out.println("ArrayIndexOutOfBoundsException 발생!!");
			}
			//try문에서 char 형태로 전환된 문자가 알파벳이 아닐 경우 
			//ArrayIndexOutOfBoundsException이 발생한다. 
			//catch문으로 예외처리하여 오류 발생 메세지를 알리고 이후 내용은 정상적으로 진행한다. 
		}

		for (int i = 0; i < Chars.length; i++) {
			if (Chars[i] != 0) {
				System.out.println("문자 " + (char) (i + 'A') + ": " + Chars[i] + "번");
			}
			//각 문자가 문자열에서 몇 번 사용되었는지를 출력한다. 
			//사용되지 않은 문자는 제외하고 출력한다. 
		}

	}
}