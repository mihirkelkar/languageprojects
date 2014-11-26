
public class find_min_in_rotated {
	public static void main(String args[]){
		int[] temp = {7, 8, 9, -4, -1, 0, 2, 3, 4, 5, 6};
		int x = find_min_rotated(temp);
		System.out.println(x);
	}
	
	public static int find_min_rotated(int[] array){
		int low = 0;
		int high = array.length - 1;
		int middle;
		while(low < high){
			middle = (low + high) / 2;
			if(array[middle - 1] <= array[middle] && array[middle] <= array[middle + 1]){
				if(array[middle] < array[array.length - 1]){
					high = middle - 1;
				}
				else if(array[middle] > array[array.length - 1]){
					low = middle + 1;
				}
			}
			else if(array[middle] <= array[middle - 1] && array[middle] <= array[middle + 1]){
				return array[middle];
			}
			
			else if(array[middle - 1] <= array[middle] && array[middle] >= array[middle + 1]){
				return array[middle + 1];
			}
		}
		return 0;
	}
}
