import java.util.ArrayList;
import java.util.List;

public class _119_PascalsTriangleII {
	class Solution {
	    public List<Integer> getRow(int rowIndex) {
	        List<List<Integer>> tra = new ArrayList<List<Integer>>();
	        List<Integer> row = new ArrayList<Integer>();
	        for(int i = 0; i<=rowIndex; i++){
	            
	            List<Integer> row2 = new ArrayList<Integer>();
	            for(int j = 0; j <=i; j++){
	                if(j==0 || j==i){
	                    row2.add(1);
	                }else{
	                    row2.add(tra.get(i-1).get(j-1)+tra.get(i-1).get(j));
	                }    
	            }
	            tra.add(row2);
	            row = row2;
	        }
	        return row;
	}
	}
}
