/*작성자: 임다희(2312282)
 *작성일: 2024-11-21
 *Lab 10-1 HashMap 활용 예제*/

import java.util.*; //자료구조 사용을 위한 패키지 import

public class ContryTest {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		Map<String, String> map = new HashMap<String, String>();
		// 국가 이름을 키, 수도를 값으로 하여 저장하는 해쉬맵을 생성한다.

		map.put("USA", "Washington");
		map.put("Japan", "Tokyo");
		map.put("China", "Beijing");
		map.put("UK", "London");
		map.put("Korea", "Seoul");
		// 해쉬맵에 5가지 데이터를 입력한다.

		Iterator<String> it = map.keySet().iterator();
		// 맵의 모든 요소를 방문하기 위해 반복자를 사용한다.

		while (it.hasNext()) {
			String key = it.next();
			System.out.println("Key: " + key + ", Value: " + map.get(key));
			// 맵의 모든 요소를 방문하며 각각의 key값과 key에 대응하는 value값을 출력한다.
		}

		System.out.print("국가 이름을 입력하시오: ");
		String name = sc.next();
		// 사용자에게 key값(국가 이름)을 입력받는다.
		System.out.println(name + "의 수도: " + map.get(name));
		// 사용자가 입력한 key값에 대응하는 value 값(수도)을 찾아 출력한다.
	}
}
