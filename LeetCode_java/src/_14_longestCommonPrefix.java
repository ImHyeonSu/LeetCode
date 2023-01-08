
public class _14_longestCommonPrefix {
	class Solution {
	    public String longestCommonPrefix(String[] strs) {
	        if(strs.length<1 || strs== null){
	            return "";
	        }
	        if(strs.length==1){
	            return strs[0];
	        }

	        int strslength = strs[0].length();
	        int strswrite = 0;

	        for(int i = 1; i < strs.length; i++){
	            int forlength = strs[i].length();
	            if(strslength>forlength){
	                strslength = forlength;
	                strswrite = i;
	            }
	            
	        }
	        String shortstrs = strs[strswrite];
	        for(int a = 0; a <strs.length; a++){
	            while(strs[a].indexOf(shortstrs) != 0){
	                shortstrs = shortstrs.substring(0, shortstrs.length()-1);                  
	            }
	            
	        }
	        return shortstrs;


	    }
	    
	}
}
