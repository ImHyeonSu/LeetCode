import java.util.HashMap;

public class _01_twoSum {
	class Solution {
	    public int[] twoSum(int[] nums, int target) {
	        HashMap<Integer,Integer> sums = new HashMap<Integer,Integer>();
	        for(int i=0;i<nums.length;i++){
	           if(sums.containsKey(nums[i])){
	               int left = sums.get(nums[i]);
	               return new int[]{left, i};
	           } else{
	               sums.put(target-nums[i],i);
	           }
	        }
	        return new int[2];
	    }
	}
}
