import java.util.HashMap;
import java.util.Scanner;
public class remove_duplicates {
	private static Scanner user_input;
	public static void main(String args []){
		user_input = new Scanner(System.in);
		System.out.println("Enter the string");
		String input = user_input.next();
		//System.out.println(input);
		System.out.println(remove_dups(input));
		
	}
	
	public static String remove_dups(String input){
	HashMap<Character, Integer> char_map = new HashMap<Character, Integer>();
	int i;
	Integer val;
	for(i = 0; i< input.length(); i++){
			val = (Integer) char_map.get(input.charAt(i));
			if(val != null){
				char_map.put(input.charAt(i), val + 1);
			}
			else{
				char_map.put(input.charAt(i), 1);
			}
		}
	String no_dups = "";
	for(i = 0; i < input.length(); i++){
		val = (Integer) char_map.get(input.charAt(i));
		if(val == 1){
			no_dups = no_dups + input.charAt(i);
		}
	}
	return no_dups;
	}
}
