import java.util.ArrayList;

public class nextsmaller {
    public ArrayList<Integer> prevSmaller(ArrayList<Integer> A) {
        int n = A.size();
        Stack<Integer> st = new Stack<>();
        // int[] ans = new int[n];
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=0;i<n;i++){
            while (!st.isEmpty() && A.get(i)<=st.peek()){
                st.pop();
            }
            if (st.isEmpty()) ans.add(-1);
            else ans.add(st.peek());
            st.push(A.get(i));
        }
        return ans;
    }
}


