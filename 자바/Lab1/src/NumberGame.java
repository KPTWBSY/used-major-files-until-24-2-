/*작성자: 임다희(2312282)
 *작성일: 2024-09-12
 *Lab1-3. 숫자 추측 게임*/

import java.lang.Math;
import java.util.Scanner;

public class NumberGame {
	public static void main(String[] args) {

		int x = (int) (Math.random() * 100);
		// 0~100 사이의 난수를 생성한다.
		int TryNum = 0;
		// 시도 횟수를 세는 변수를 생성한다.
		Scanner sc = new Scanner(System.in);

		while (true) {
			// 조건을 만족해 break문이 활성화되기 전까지 계속 while문을 실행한다.
			System.out.print("정답을 추측하여 보시오 >> ");
			// 사용자 입력을 위한 메세지를 출력한다.
			int y = sc.nextInt();
			// 사용자에게 정수를 입력받는다.
			++TryNum;
			// 시도 횟수를 증가시킨다.

			if (x > y) {
				System.out.println("Up");
			}
			// 사용자가 입력한 수가 랜덤으로 생성된 0~100 사이의 난수보다 작을 경우
			// "Up"이라는 메세지를 출력한다.
			else if (x < y) {
				System.out.println("Down");
			}
			// 사용자가 입력한 수가 랜덤으로 생성된 0~100 사이의 난수보다 클 경우
			// "Down"이라는 메세지를 출력한다.

			else {
				System.out.println("축하합니다. 시도횟수=" + TryNum);
				break;
			}
			// 사용자가 입력한 수가 랜덤으로 생성한 0~100 사이의 난수와 같을 경우
			// 축하 메세지와 시도 횟수를 출력하고 while문 루프를 종료한다.
		}
	}
}
