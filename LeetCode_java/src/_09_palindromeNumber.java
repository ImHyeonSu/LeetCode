
public class _09_palindromeNumber {
	class Solution {
		public boolean isPalindrome(int x) {
		    int tmp = x, cache = 0;
		    while(tmp > 0){
		        cache = cache*10 + tmp % 10;
		        tmp /= 10;
		    }
		    return x >= 0 && cache == x;
		}
		    }

}
