public class Minstack {
    int n=0;
    Stack<Long> st = new Stack<>();
    Long min = Long.MAX_VALUE;

    public void push(int value){
        Long val = Long.valueOf(value);
        if (st.isEmpty()){
            min = val;
            st.push(val);
        }
        else{
            if(val<min){
                st.push(2*val - min);
                min = val;
            }
            else{
                st.push(val);
            }
        }
    }


    public void pop(){
        if(st.isEmpty()){
            throw new IllegalStateException("empty stack");

        }
        Long  val = st.pop();
        if (val<min){
            min = 2*min - val;
        }
        
    }


    
 
}

