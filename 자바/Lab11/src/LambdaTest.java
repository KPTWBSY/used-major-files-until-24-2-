import java.util.*;

public class LambdaTest {
	public static void main(String[] args) {
		
		List<String> list1=Arrays.asList("Apple","Banana","Pear","Cherry");
		List<String> list2=new ArrayList<>();
		for(String string: list1) {
			if(string.equals("Apple")||string.equals("Cherry")) {
				list2.add(string);
			}
		}
		
		List<String> list3=new ArrayList<>();
		for(String string:list2) {
			list3.add(string+"(Fruits)");
		}
	}
}

/* 
스트림 API 사용해서 바꾼거..

import java.util.*;
import java.util.stream.Collectors;

public class LambdaTest {
    public static void main(String[] args) {
        List<String> list1 = Arrays.asList("Apple", "Banana", "Pear", "Cherry");
        
        // 람다식과 스트림 사용
        List<String> list2 = list1.stream()
                                  .filter(string -> string.equals("Apple") || string.equals("Cherry"))
                                  .collect(Collectors.toList());
        
        List<String> list3 = list2.stream()
        							.map(string -> string + "(Fruits)")
        							.collect(Collectors.toList());
    }
}*/


