/*작성자: 임다희(2312282)
 *작성일: 2024-11-29
 *Lab 11-1 MethodReferenceLowerCase*/

import java.util.*;
import java.util.stream.*;

//String의 리스트를 받아서 소문자로 변환한 후 새로운 리스트로 반환하는 코드.
public class MethodReferenceLowerCase {

	public static void main(String[] args) {
		List<String> listOfNames =Arrays.asList(new String[]
				{"Apple","Banana","Cherry"});
		//String 타입의 리스트 listOfNames.
		//Arrays.asList() 메서드를 사용해 {"Apple","Banana","Cherry"} 배열을 리스트로 변경.
		
		List<String> collect1 = listOfNames.stream()
		//listOfNames 리스트에서 스트림을 생성한다. 
					.map(s->s.toLowerCase())
		//map() 메서드를 통해 listOfNames의 각 요소(문자열)를 toLowerCase 메서드로
		//소문자로만 이루어진 문자열이 되도록 변환한다.
					.collect(Collectors.toList());
		//스트림의 결과를 컬렉션으로 변환하는 collect() 메서드를 통해 결과를 collect1에 저장한다. 
		
		System.out.println(collect1);
		//최종적으로 변환된 리스트 collect1을 출력한다. 

	}

}
