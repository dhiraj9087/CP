import java.util.Stack;

public class Solution {
    public int[] nextSmallerElement(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];  // Array to store the result
        Stack<Integer> st = new Stack<>();  // Stack to store indices

        for (int i = 0; i < n; i++) {
            // While the stack is not empty and the current element is smaller than
            // the element corresponding to the index stored at the top of the stack
            while (!st.isEmpty() && arr[i] < arr[st.peek()]) {
                int index = st.pop();
                result[index] = arr[i];
            }
            // Push the current index onto the stack
            st.push(i);
        }

        // For elements that have no next smaller element, set their value to -1
        while (!st.isEmpty()) {
            result[st.pop()] = -1;
        }

        return result;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] arr = {4, 8, 5, 2, 25};
        int[] res = sol.nextSmallerElement(arr);
        for (int r : res) {
            System.out.print(r + " ");
        }
    }
}
