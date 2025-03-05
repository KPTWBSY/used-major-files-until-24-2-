/*작성자: 임다희(2312282)
 *작성일: 2024-10-20
 *Lab6-4 InputSumTest 클래스*/

import java.util.Scanner;

public class InputSumTest {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.print("여러 개의 정수 입력: ");
		String inputString = sc.nextLine(); 
		//사용자에게 문자열을 입력받는다. 
		
		String splitStrings[] = inputString.split(" ");
		//사용자에게 입력받은 문자열을 띄어쓰기 단위로 분리해 배열에 저장한다.

		int sum = 0; //사용자에게 입력받은 숫자들의 합을 나타내는 변수. 

		for (int i = 0; i < splitStrings.length; i++) {

			try {
				int num = Integer.parseInt(splitStrings[i]);
				//배열에 저장된 문자열을 정수 형태로 바꾸는 시도.
				sum += num; //변경된 정수를 숫자들의 합에 더한다. 
			}

			catch (NumberFormatException num) {
				System.out.println("NumberFormatException 발생!");
				//배열에 저장된 문자열을 정수 형태로 바꿀 수 없는 경우 
				//NumberFormatException이 발생하므로 해당 경우 catch문으로 예외처리하여
				//오류 발생을 알리고 다음 반복문을 계속해서 실행한다.  
			}
		}
		System.out.print("정수들의 합은 " + sum); //정수들의 합을 출력한다. 
	}

}
