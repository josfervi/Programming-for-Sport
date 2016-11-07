public class Solution {
    // public static void main(String[] args) {
    //     System.out.println( power("000001")
    // }
    
	public int power(String a) {
	    
	    int len= a.length();
	    
	    int i= 0;
	    while ( i < len && a.charAt(i) == '0' ) {
	        i++;
	    }
	    a= a.substring(i);
	    
	    if ( a.equals("") || a.equals("1") ) {
	        return 0;
	    }
	    
	    // { A is a String of digits }
	    int[] a_arr= new int[len];
	    for (i= 0; i<len; i++) {
	        a_arr[i]= a.charAt(i) - '0'; // '0' becomes 0
	                                     // '1' becomes 1
	                                     // ...
	                                     // '9' becomes 9
	    }
	    // { A_arr is an array of ints, each in [0...9] }
	    
	    Boolean carry_flag= false;
	    
	    while ( a_arr[len -1] % 2 == 0 ) {
	        
	        int tmp;
	        for (i= 0; i<len; i++) {
	            tmp= a_arr[i];
	            a_arr[i]= tmp/2 + (carry_flag? 5 : 0);
	            carry_flag= tmp % 2 == 1;
	        }
	    }
	    
	    i= 0;
	    while ( i<len  &&  a_arr[i]==0 ) {
	        i++;
	    }
	    a_arr= Arrays.copyOfRange(a_arr, i, len);

	    if ( a_arr.length == 1  &&  a_arr[0] == 1 ) {
	        return 1;
	    }
	    return 0;
	}
}