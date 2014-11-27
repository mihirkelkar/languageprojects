//find the first occurence of an element in a sorted array. 
public class first_occurence_sorted_arrays {
	public static void main(String args[]){
		int[] array = {1, 2, 3, 55, 55, 55, 76, 76, 88, 99};
		int index = binary_search(array, 0, array.length - 1, 55);
		System.out.println(index);
	}

	public static int binary_search(int[] array, int low, int high, int value){
		int middle;
		while(low <= high){
			middle = (low + high) / 2;
			if(array[middle] == value){
				int result = binary_search(array, low, middle - 1, value);
				if(result != -1){
					return result;
				}
				else{
					return middle;
				}
				
			}
			else if(array[middle] > value){
				high = middle - 1;
			}
			else if(array[middle] < value){
				low = middle + 1;
			}
		}
		return -1;
	}
	
}
