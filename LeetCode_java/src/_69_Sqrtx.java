
public class _69_Sqrtx {
	class Solution {
	    public int mySqrt(int x) {
			long a = 0; 
			long b = 0;
			while(b < x) {
				a++;
				b = a*a;			
			}
			if(b <= x) {
				return (int)a;
			}else if(b>x) {
				return (int)a-1;
			}
	        return (int)a;
	}
	}
}
