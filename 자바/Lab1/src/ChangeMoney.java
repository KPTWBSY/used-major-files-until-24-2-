
/*작성자: 임다희(2312282)
 *작성일: 2024-09-12
 *Lab1-2. 동전 변환 예제*/

import java.util.Scanner;

public class ChangeMoney {

	public static void main(String[] args) {
		System.out.print("금액을 입력하시오 >>");
		// 사용자 입력을 받기 위한 메세지를 출력한다.
		Scanner sc = new Scanner(System.in);

		int x;
		x = sc.nextInt();
		// 사용자로부터 정수를 입력받는다.
		int[] unit = { 50000, 10000, 5000, 1000, 500, 100, 50, 10, 1 };
		// 돈 액수로 구성된 배열을 생성한다.

		for (int i = 0; i < unit.length; i++) {
			// 배열의 모든 원소에 대해 사용자로부터 입력받은 정수가
			// 배열의 i번째 원소로 나누어떨어지는지 검사한다.
			if (x / unit[i] != 0) {
				// 조건에 해당할 경우 입력받은 정수를 배열의 i번째 원소로 나눈 몫을 출력한다.
				// 기존에 입력받은 정수 값은 해당 값을 배열의 i번째 원소로 나눈 나머지로 초기화된다.
				System.out.println(unit[i] + "원 짜리 : " + x / unit[i]);
				x = x % unit[i];

			}

		}

	}

}
