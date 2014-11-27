import java.util.Scanner;
public class reverse_number {
	public static void main(String args[]){
		int num = Integer.parseInt(new Scanner(System.in).next());
		int number = reverse_num(num);
		System.out.println(number);
	}
	
	public static int reverse_num(int number){
		int result  = 0;
		int temp_number;
		int flag = 0;
		if(number < 0){
			number = number * -1;
			flag = 1;
		}
		while(number > 0){
			temp_number = number % 10;
			result = result * 10 + temp_number;
			number = number / 10;
		}
		if(flag == 1){
			return result * -1;
		}
		return result;
		
	}
}
