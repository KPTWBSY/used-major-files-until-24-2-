/*작성자: 임다희(2312282)
 *작성일: 2024-11-29
 *Lab 11-3 Test*/

import java.util.*;
import java.util.stream.*;

public class Test {

	public static void main(String[] args) {
		List<Color> list =new ArrayList<>(); //Color 객체를 저장하는 객체 배열 list
		Color red =new Color("Red","#FF0000");
		Color blue = new Color("Blue","0000FF");
		Color white = new Color("White","FFFFFF");
		Color green =new Color("Green", "008000");
		//Color 객체를 4개 생성한다.
		
		list.add(red);
		list.add(blue);
		list.add(white);
		list.add(green);
		//list에 생성한 4개의 Color 객체를 추가한다. 
		
		List <String> resultList = list.stream()
		//list에서 스트림을 생성한다. 
			.map(Color::getName) 
			//매핑 연산으로 list 내의 Color 객체를 해당 객체의 이름(String) 값으로 변환한다.
			.sorted() //이름(String) 값끼리 비교하여 알파벳순으로 정렬되도록 한다. 
			.collect(Collectors.toList());
		//스트림의 결과를 컬렉션으로 변환하는 collect() 메서드를 통해 결과를 resultList에 저장한다.
		
		resultList.forEach(System.out::println);
		//최종적으로 resultList(String 타입을 저장하는 리스트)에 들어있는 요소들을 차례대로 출력한다. 
	}

}

class Color{ //Color 클래스. 
		String name; //색의 이름을 나타내는 String 타입의 필드 name
		String hexaCode; //색의 코드를 나타내는 String 타입의 필드 hexaCode
		public String getName() { //name의 접근자.
			return name;
			}
		public void setName(String name) { //name의 변경자
				this.name=name;
		}
		@Override
		public String toString() { //Color 객체의 필드 정보를 문자열로 반환하는 메서드. 
				return "Color [name="+name+", hexaCode="+hexaCode+"]";
		}
		public String getHexaCode() { // hexaCode의 접근자
				return hexaCode;
		}
		public void setHexaCode(String hexaCode) { //hexaCode의 변경자
				this.hexaCode=hexaCode;
		}
		public Color(String name, String hexaCode) { //Color 객체의 생성자
				super();
				this.name=name;
				this.hexaCode=hexaCode;
		}
}
