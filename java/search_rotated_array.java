//Search an element in a rotated array. 
public class search_rotated_array {
	public static void main(String args[]){
		int[] temp = {18, 23, 45, 5, 6, 7, 8, 9, 11, 13, 14, 16};
		Object number = find_number(temp, 5);
		if(number == null){
			System.out.println("Number not found");
		}
		else{
			System.out.println("Number found at index" + number);
		}
		System.out.println("Exectuion ends");
	}
	
	public static int find_min(int[] array){
		int low = 0;
		int high = array.length - 1;
		int middle;
		while(low < high){
			middle = (low + high) / 2;
			//Landing on the pivot element
			if(array[middle] <= array[middle + 1] && array[middle] <= array[middle - 1]){
				return middle;
			}
			//Landing on the element before the pivot
			else if(array[middle - 1] <= array[middle] && array[middle] > array[middle + 1]){
				return middle + 1;
			}
			
			else if(array[middle - 1] <= array[middle] && array[middle] <= array[middle + 1]){
				if(array[middle] < array[array.length - 1]){
					high = middle - 1;
				}
				else{
					low = middle + 1;
				}
			}
		}
		return -1;
	}
	
	public static int binary_search(int[] array, int low, int high, int value){
		int middle;
		while(low <= high){
			middle = (low + high) / 2;
			if(array[middle] == value){
				return middle;
			}
			else if(array[middle] < value){
				low = middle + 1;
			}
			else if(array[middle] > value){
				high = middle - 1;
			}
		}
		return -1;
	}
	
	public static Object find_number(int[] array, int value){
		//int low = 0;
		//int high = array.length - 1;
		//int middle;
		//Finding the index of the pivot element from which the second sorted array starts. 
		int result;
		int pivot = find_min(array);
		if(value >= array[pivot] && value <= array[array.length - 1]){
			result = binary_search(array, pivot, array.length - 1, value);
		}
		else{
			result = binary_search(array, 0, pivot - 1, value);
		}
		if(result != -1){
			return result;
		}
		return null;
	}
}	