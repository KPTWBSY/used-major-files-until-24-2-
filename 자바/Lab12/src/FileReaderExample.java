/*작성자: 임다희(2312282)
 *작성일: 2024-12-05
 *Lab 12-1 FileReaderExample*/

import java.io.FileReader;
import java.io.IOException;

/*test.txt의 내용(총 5줄)
 * 
 * 2024/12/05
 * this is a test
 * 2312282
 * java programming
 * read test.txt
 * 
 * 위 내용과 같다. 
 */

public class FileReaderExample {

	public static void main(String[] args) {
		try (FileReader fr = new FileReader("test.txt")){
		//FileReader를 통해 test.txt의 내용을 읽어온다. 
			int ch;
			while((ch=fr.read())!=-1)
				System.out.print((char) ch);
		//test.txt의 내용을 한 글자씩 읽어와 출력한다. 
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
