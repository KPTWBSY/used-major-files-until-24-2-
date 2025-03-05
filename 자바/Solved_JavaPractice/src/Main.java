/*import java.util.Scanner;
public class BOJ_1271 {
	
	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		
		int x,y;
		x=sc.nextInt();
		y=sc.nextInt();
		
		System.out.println(x/y);
		System.out.println(x%y);
		}
	
}*/

import java.util.Scanner;
import java.math.BigInteger;
public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		
		BigInteger x=sc.nextBigInteger();
		BigInteger y=sc.nextBigInteger();
		
		System.out.println(x.divide(y));
		System.out.println(x.remainder(y));
		}
	
}