/*작성자: 임다희(2312282)
 *작성일: 2024-12-05
 *Lab 12-2 CopyLines*/

import java.io.*;

public class CopyLines {
	public static void main(String[] args) {
		try (BufferedReader in = new BufferedReader(new FileReader("test.txt"));
			//test.txt의 내용을 BufferedReader를 통해 읽는다. 
				PrintWriter out = new PrintWriter(new FileWriter("output.txt"))){
			//PrintWriter를 통해 output.txt에 내용을 작성한다. 
					String line; //test.txt에서 읽어온 한 줄(문자열)
					int linenumber=1; //줄번호를 나타내는 정수
					while((line=in.readLine())!=null) {
				//test.txt에서 한 줄을 읽어온 결과가 null이 아닌 동안
						out.println(linenumber+" "+line);
				//줄번호와 함께 읽어온 문자열의 내용을 출력시킨다.
						linenumber++;
				//다음 줄 출력에 대비해 줄번호를 1만큼 증가시킨다. 
					}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
