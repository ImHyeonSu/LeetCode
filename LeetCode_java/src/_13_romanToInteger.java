import java.util.HashMap;

public class _13_romanToInteger {
	class Solution {
	    public int romanToInt(String s) {
	        HashMap<Character,Integer> map = new HashMap<>();
			    map.put('M', 1000);
			    map.put('D', 500);
			    map.put('C', 100);
			    map.put('L', 50);
			    map.put('X', 10);
			    map.put('V', 5);
			    map.put('I', 1);		
			int befores, afters = 0;
			int result=0;
			for(int a= 0; a<s.length(); a++) {
			 befores = afters;
			 afters= map.get(s.charAt(a));
			 if(afters>befores && a>0) {
				result+=(afters-(befores*2));
			 }else {
				 result+=afters;
			 }
			}
	        return result;
	}
	}
}
