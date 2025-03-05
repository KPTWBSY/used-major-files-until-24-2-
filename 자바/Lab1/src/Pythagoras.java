/*작성자: 임다희(2312282)
 *작성일: 2024-09-12
 *Lab1-4. 피타고라스의 정리*/

public class Pythagoras {
	public static void main(String[] args) {

		int a, b, c;
		// 필요한 정수형 변수 3개를 선언한다.
		for (a = 1; a <= 30; a++) {
			for (b = 1; b <= 30; b++) {
				for (c = 1; c <= 30; c++) {
					// 각 정수의 값을 1부터 시작해 30보다 작거나 같을 때까지 1씩 더해가며 검사한다.
					if (a * a + b * b == c * c && a <= b) {
						// a,b,c가 피타고라스 정리를 만족하고
						// a,b의 값만 서로 바뀌고 c는 그대로인 중복된 결과를 방지하기 위해
						// a<=b라는 조건을 추가로 걸어 해당 조건을 모두 만족하면
						System.out.println(a + "   " + b + "   " + c);
						// a b c 의 값을 출력한다.
					}

				}
			}
		}
	}
}
