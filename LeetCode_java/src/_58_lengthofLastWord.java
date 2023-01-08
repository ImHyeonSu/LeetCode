
public class _58_lengthofLastWord {
	class Solution {
	    public int lengthOfLastWord(String s) {
	        String[] neos = s.split("\\s+");
	        String ss = neos[neos.length-1];
	        return ss.length();
	    }
	}
}
