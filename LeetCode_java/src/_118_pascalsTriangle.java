import java.util.ArrayList;
import java.util.List;

public class _118_pascalsTriangle {
	class Solution {
	    public List<List<Integer>> generate(int numRows) {
	        List<List<Integer>> tra = new ArrayList<List<Integer>>();
	        if (numRows <= 0){
	            return tra;
	        }
	        for(int i = 0; i <numRows ; i++){
	            List<Integer> row = new ArrayList<Integer>();
	            for(int j=0; j<=i; j++){
	                if(j==0 || j==i){
	                    row.add(1);
	                }else{
	                    row.add(tra.get(i-1).get(j-1)+tra.get(i-1).get(j));
	                }
	            }
	            tra.add(row);
	        }
	        return tra;
	    }
	}
}
