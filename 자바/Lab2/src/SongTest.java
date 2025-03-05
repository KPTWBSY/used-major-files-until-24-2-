/*작성자: 임다희(2312282)
 *작성일: 2024-09-19
 *Lab2-2. Song 클래스 작성*/

//Song 클래스.
class Song {
	
	private String title,artist;
	private int length;
	//private 형태의 필드 선언. 
	
	public Song(String title, String artist, int length) {
		
		this.title=title;
		this.artist=artist;
		this.length=length;
	} //생성자 (기본 형태, 변수 3개가 모두 들어옴)
	
	public Song() {
		this("정보 없음", "정보 없음", 0);
	} //다른 경우의 생성자 중복 정의(title, artist, length 중 아무것도 들어오지 않음)
	
	public Song(String title) {
		this(title,"정보 없음",0);
	} //다른 경우의 생성자 중복 정의(title 이외의 변수가 들어오지 않음)
	
	public Song(String title, String artist) {
		this(title,artist,0);
	} //다른 경우(title,artist의 변수만 들어오고 length 값은 들어오지 않음)
	
	
	public String toString() {
		return String.format("Song [제목: %s, 가수: %s, 곡의 길이 : %s]",title, artist, length);		
	} //title, artist, length의 필드 정보를 담은 문자열을 출력하는 메소드 toString.
}

//SongTest 클래스
public class SongTest {

	public static void main(String[] args) {
		Song s1=new Song("Outward Bound", "NaNa", 180); //매개변수 3개가 모두 들어간 경우
		Song s2=new Song("Jambalya", "Capenters"); //length 값이 들어가지 않은 경우
		Song s3=new Song("Yesterday"); //title 값만 들어간 경우
		Song s4=new Song(); //어떤 값도 들어가지 않은 경우
		
		//각 경우에 대해 필드 정보를 담은 문자열을 출력한다. 
		System.out.println(s1);
		System.out.println(s2);
		System.out.println(s3);
		System.out.println(s4);
	}

}
