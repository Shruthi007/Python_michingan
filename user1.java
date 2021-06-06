import ComplexOperation.*;
import java.util.*;
public class user1
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("ENTER THE NUMBER TO BE CHECKED-");
		int x=sc.nextInt();
		checkPrime u= new checkPrime();
		System.out.println(u.testPrime(x));
	}
}
