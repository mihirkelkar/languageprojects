//Given an integer, find the lowest power of 2 greater than the given number. 
//Solution, right shift the number till it is 0, get a variable called result and left shift it that many times. 
import java.util.Scanner;
public class next_power_of_two {
	public static void main(String args[]){
		Scanner temp = new Scanner(System.in);
		int number = Integer.parseInt(temp.next());
		System.out.println(find_next_power_of_two(number));
	}
	
	public static int find_next_power_of_two(int number){
		int result = 1;
		while(number != 0){
			number >>= 1;
			result <<= 1;
		}
		return result;
	}
}
