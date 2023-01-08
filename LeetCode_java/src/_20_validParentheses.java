import java.util.Stack;

public class _20_validParentheses {
	class Solution {
	    public boolean isValid(String s) {
			Stack<Character> stack = new Stack<>();
			for(int a = 0; a<s.length(); a++) {
				char checkword=s.charAt(a);
				if(checkword =='('||checkword =='{'||checkword =='[') stack.push(checkword);
				else if(stack.empty()) return false;
				else if(checkword ==')'&& stack.pop() != '(') return false;
				else if(checkword =='}'&& stack.pop() != '{') return false;
				else if(checkword ==']'&& stack.pop() != '[') return false;
			}
			return stack.empty(); 
		}

	    }

}
