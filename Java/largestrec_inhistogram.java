public class largestrec_inhistogram {

        public int largestRectangleArea(int[] heights) {
            int n = heights.length;
            Stack<Integer> st = new Stack<>();
            Stack<Integer> st2 = new Stack<>();
            // int[] ans = new int[n];
            int[] pse = new int[n];
            int[] nse = new int[n];
            int ind=0;
            for(int i=n-1;i>=0;i--){
                while(!st.isEmpty() && heights[st.peek()]>=heights[i]){
                    st.pop();
                }
                if (!st.isEmpty()){
                    nse[i] = st.peek();
                }
                else{
                    nse[i] = n;
                }
                st.push(i);
            }
            
    
            for(int i=0;i<n;i++){
                while(!st2.isEmpty() && heights[st2.peek()]>heights[i]){
                    st2.pop();
                }
                if (!st2.isEmpty()){
                    pse[i] = st2.peek();
                }
                else{
                    pse[i] = -1;
                }
                st2.push(i);
            }
            for(int i=0;i<n;i++){
                System.out.print(nse[i]);
                
            }
            for(int i=0;i<n;i++){
                System.out.print(pse[i]);
                
            }
            int ans=0;
            for(int i=0;i<n;i++){
                ans = Math.max(ans,heights[i]*(nse[i]-pse[i]-1));
            }
            return ans;
        }
    }

