
public class _70_climbingStairs {
	class Solution {
	    public int climbStairs(int n) {
	        if(n == 1){
	            return 1;
	        }else if(n ==2){
	            return 2;
	        }
	        int prevPrev = 1;
	        int prev =2;
	        int curr = 0;
	        for(int i = 3; i<=n; i++ ){
	            curr = prevPrev+prev;
	            prevPrev = prev;
	            prev = curr;
	        }
	            return curr;
	    }
	}
}
