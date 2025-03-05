/*작성자: 임다희(2312282)
 *작성일: 2024-09-12
 *Lab1-5. 랜덤 배열 생성*/

import java.lang.Math;

public class RandomArray {
	public static void main(String[] args) {
		// 모든 원소가 0으로 초기화된 3*5 크기의 2차원 배열을 생성한다.
		int[][] randomArray = { { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 } };
		// 원소 중 1로 바뀐 원소의 개수를 샐 변수를 생성한다.
		int numOfOne = 0;

		while (true) {

			if (numOfOne == 5) {
				break;
			}
			// 1의 개수가 5개이면 while문 루프를 종료한다.

			int x = (int) (Math.random() * 3);
			int y = (int) (Math.random() * 5);
			// 랜덤한 행의 번호를 나타내는 0~2 사이의 난수 x,
			// 랜덤한 열의 번호를 나타내는 0~5 사잉의 난수 y를 생성한다.

			if (randomArray[x][y] == 0) {
				randomArray[x][y] = 1;
				numOfOne++;
			}
			// 생성한 난수 x,y값을 각각 배열의 행, 열 값에 대입해
			// 해당 위치에 해당하는 배열의 원소가 0이면 1로 바꾼다.
			// 1의 개수도 1만큼 증가시킨다.
		}

		for (int i = 0; i < randomArray.length; i++) {
			for (int j = 0; j < randomArray[i].length; j++) {
				System.out.print(randomArray[i][j]);
			}
			System.out.println("");
		}
		// 생성된 배열을 출력한다.
	}
}
