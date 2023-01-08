
public class _35_searchInsertPosition {
	class Solution {
	    public int searchInsert(int[] nums, int target) {
	        int left = 0;
	        int right = nums.length - 1;
	        int mid = 0;

	        while(left <= right){
	            if(target<nums[left]) return left;
	            if(target>nums[right])return right+1;
	            mid = (left+right)/2;

	            if(nums[mid]== target) return mid;
	            else if(nums[mid]>target){
	                right = mid -1 ;
	            }else{
	                left = mid+1;
	            }

	        }
	        return -1;

	    }
	}
}
