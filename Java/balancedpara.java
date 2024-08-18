public class balancedpara {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(char i:s.toCharArray()){
            if (i=='(' || i=='{' || i=='['){
                stack.push(i);
            }
            else {
                if (stack.isEmpty()){
                    return false;
                }
                char top = stack.peek();
                if ((i==')' && top=='(') || (i==']' && top=='[') || (i=='}' && top=='{')){
                    stack.pop();
                }
                else{
                    return false;
                }
            }




        }
        return stack.isEmpty();
    }
} 
