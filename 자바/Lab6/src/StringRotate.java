/*작성자: 임다희(2312282)
 *작성일: 2024-10-20
 *Lab6-2 StringRotate 클래스*/

import java.util.Scanner;

public class StringRotate { //StringRotate 클래스. 

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.println("문자열을 입력하세요. 빈 칸이나 있어도 되고 영어 한글 모두 됩니다.");
		String rotateString = sc.nextLine();
		//사용자에게 문자열을 입력받는다. 

		for (int i = 0; i < rotateString.length() - 1; i++) {
			System.out.print(rotateString.substring(i + 1));
			System.out.println(rotateString.substring(0, i + 1));
			//for문과 substring 메소드를 이용해 i(0~입력받은 문자열의 길이)+1번째부터  
			//문자열 끝까지의 부분 문자열, 그리고 해당 문자열에 포함되지 않은 앞부분의 나머지 문자열
			//(0번째~i번째 를 함께 붙여 출력한다. 
		}
		System.out.println(rotateString);
		//마지막으로는 원본 문자열을 출력한다. 
	}
}
