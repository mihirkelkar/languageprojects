import java.util.Scanner;
import java.util.ArrayList;
//Given a string abbadefdexy. Find the substrings which are palindorme 
//In this case, this would be bb, abba, defde etc

public class Palindome_Substrings {
	private static Scanner user_input;

	public static void main(String args[]){
		user_input = new Scanner(System.in);
		String input = user_input.next();
		ArrayList<String> temp = palindrome_finder(input);
		System.out.println(temp);
		System.out.println("Exectuion complete");
	}
	
	public static ArrayList<String> check_palindrome(String input, int start){
		int end = start;
		int total_length = input.length();
		ArrayList<String> palindromes = new ArrayList<String>();
		while(start >= 0 && end < total_length){
			System.out.println(input.charAt(start) + " " + input.charAt(end));
			if(input.charAt(start) == input.charAt(end)){
				palindromes.add(input.substring(start, end + 1));
				System.out.println(input.substring(start, end + 1));
				start -= 1;
				end += 1;
			} 
			else{
				break;
			}
		}
		return palindromes;
	}
	
	public static ArrayList<String> palindrome_finder(String input){
		ArrayList<String> palindromes = new ArrayList<String>();
		int i;
		for(i = 1; i < input.length(); i++){
		  palindromes.addAll(check_palindrome(input, i));
		}
		return palindromes;
	}
}
