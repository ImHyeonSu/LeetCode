
public class _67_addBinary {
	class Solution {
	    public String addBinary(String a, String b) {
	        StringBuilder result = new StringBuilder();
	        int sum = 0; 
	        int carry = 0;
	        int alength = a.length()-1;
	        int blength = b.length()-1; 

	        while(alength >= 0 || blength >=0){
	            int bita = (alength >= 0) ? Integer.parseInt(String.valueOf(a.charAt(alength))) : 0;
	            int bitb = (blength >= 0) ? Integer.parseInt(String.valueOf(b.charAt(blength))) : 0;
	            sum= carry ^ bita ^ bitb; // 3 - sum 1 carry 0  2 - sum 0 carry 1  1 - sum 1 carry 0 //0 - sum  0 carry 1 
	            carry = (carry & bita) | (carry & bitb) | (bita & bitb);
	            result.append(String.valueOf(sum));
	            alength --;
	            blength --;
	        }
	        if(carry>0)
	            result.append(String.valueOf(carry));
	        
	        return result.reverse().toString();

	    }
	}
}
