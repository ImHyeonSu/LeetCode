
public class _27_removeElement {

class Solution {
    public int removeElement(int[] nums, int val) {
        int i=0;
    for(int j=0; j<nums.length;j++) {
        if (nums[j] != val) {
            nums[i]=nums[j];        //j = 0 / j = 1 - nums[0] <nums[1] i==1 / j = 2 - nums[1] < nums[2] i ==2  
            i++;
        }
    }
    return i;
    }
}
}
