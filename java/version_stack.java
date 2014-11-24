//Implement a version stack. 
//So basically, after every push and pop, the stack maintains a copy of its present state and calls itself version X. 

import java.util.ArrayList;
import java.util.HashMap;
public class version_stack {
  static ArrayList <Integer> version_stack = new ArrayList<Integer>();
  static HashMap<Integer, ArrayList<Integer>> version_map = new HashMap<Integer, ArrayList<Integer>>();
  
  public static void main(String args []){
	  version_map.put(0, null);
	  add(2);
	  add(3);
	  pop();
	  System.out.println(version_map.get(1));
	  System.out.println("Execution Ended");
  }
  
  public static void add(int value){
	  version_stack.add(value);
	  @SuppressWarnings("unchecked")
	ArrayList<Integer> temp = (ArrayList<Integer>) version_stack.clone();
	  version_map.put(version_stack.size(), temp);
	  System.out.println(version_map.get(version_stack.size()));
  }
  
  public static int pop(){
	  int temp = version_stack.get(version_stack.size() - 1);
	  version_stack.remove(version_stack.size() - 1);
	  @SuppressWarnings("unchecked")
	ArrayList<Integer> tempstack = (ArrayList<Integer>) version_stack.clone();
	  version_map.put(version_stack.size(), tempstack);
	  return temp;
  }
    
}
