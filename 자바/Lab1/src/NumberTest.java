
/*작성자: 임다희(2312282)
 *작성일: 2024-09-12
 *Lab1-1. 자릿수별 숫자 비교*/

import java.util.Scanner;

public class NumberTest {
	public static void main(String[] args) {

		// 사용자 입력을 위한 메세지를 출력한다.
		System.out.print("2자리수 정수 입력(10~99)>>");
		Scanner sc = new Scanner(System.in);

		int x;
		x = sc.nextInt();
		// 사용자에게 정수를 입력받는다.

		if (x / 10 == x % 10) { // 10의 자리 숫자와 1의 자리 숫자가 같은지 판단한다.
			// 판단 결과에 따라 다른 메세지를 출력한다.
			System.out.println("Yes! 10의 자리와 1의 자리가 같습니다.");
		} else {
			System.out.println("No! 10의 자리와 1의 자리가 다릅니다.");
		}

	}
}
