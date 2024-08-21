/**
 * astroidcollsion
 */ 
//-11 ,-2 19 ,37 64 ,-18

public class astroidcollsion {

    public int[] asteroidCollision(int[] arr){
        int n = arr.length;
        Stack<Integer> st = new Stack<>();
        for(int i=0;i<n;i++){
                boolean alive = true;
                while(!st.isEmpty() && arr[i]<0 && st.peek()>0){
                    if (st.peek() < -arr[i]){
                        st.pop();
                        continue;
                    }
                    else if(st.peek() == -arr[i]){
                        st.pop();
                    }
                    alive = false;
                    break;
                }
                if (alive){
                    st.push(arr[i]);
                }
            }
            int[] ans = new int[st.size()];
            for(int i=st.size()-1;i>=0; --i){
                ans[i] = st.pop();
            }
            return ans;
        }
    }
