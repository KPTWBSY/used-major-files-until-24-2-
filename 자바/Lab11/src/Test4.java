/*작성자: 임다희(2312282)
 *작성일: 2024-11-29
 *Lab 11-4 Test4*/

import java.util.*;
import java.util.stream.*;

public class Test4 {
	static List<String> list=Arrays.asList("Kim","Park","He","I","Lee","Hello","World");
	//String 타입의 리스트 list
	//Arrays.asList() 메서드를 사용해 배열을 리스트로 변경.
	
	public static void main(String[] args) {
		
		String result = list.stream()
				//list에서 스트림을 생성한다. 
				.filter(s->s.length()>=3)
				//filter 메서드를 사용해 list의 요소 중 길이가 3 이상인 문자열만을 선별한다.
				.map(s->s.toUpperCase())
				//map 메소드를 이용해 선별된 요소들의 모든 문자를 toUpperCase 메소드로 대문자화한다.
				.collect(Collectors.joining(" "));
				//collect() 메서드를 통해 결과를 result에 저장한다.
			//result는 하나의 문자열이므로 스트림에서 만들어진 여러 개의 문자열을 Collectors.joining(" ")을 통해
			//stream 결과를 공백으로 구분하여 하나의 문자열로 연결한 후 저장한다. 
				
		System.out.println(result);
		//최종적으로 저장된 문자열 result를 출력한다. 
	}
}
