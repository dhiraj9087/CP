public class sumofsubarraymin {
        public int sumSubarrayMins(int[] arr) {
            int n = arr.length;
            int[] ple = new int[n];  // previous less element
            int[] nle = new int[n];  // next less element
            Stack<Integer> stack = new Stack<>();
            
            // Calculate Previous Less Element (PLE)
            for (int i = 0; i < n; i++) {
                while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                    stack.pop();
                }
                ple[i] = stack.isEmpty() ? -1 : stack.peek();
                stack.push(i);
            }
            
            stack.clear();  // Clear the stack for the next calculation
            
            // Calculate Next Less Element (NLE)
            for (int i = n - 1; i >= 0; i--) {
                while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                    stack.pop();
                }
                nle[i] = stack.isEmpty() ? n : stack.peek();
                stack.push(i);
            }
            
            // Calculate the result
            int ans = 0;
            int MOD = 1_000_000_007;  // Use modulo to prevent overflow
            for (int i = 0; i < n; i++) {
                int leftCount = i - ple[i];
                int rightCount = nle[i] - i;
                ans = (ans + arr[i] * leftCount * rightCount) % MOD;
            }
            
            return ans;
        }
    }

