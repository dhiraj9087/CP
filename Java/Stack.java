public class Stack<T> {
    private Object[] elements;
    private int size;
    private static final int DEFAULT_CAPACITY = 10;

    public Stack(){
        elements = new Object[DEFAULT_CAPACITY];
        size = 0;
    }

    public void push(T item){
        if (size >= DEFAULT_CAPACITY - 1){
            System.out.println("Stack Overflow");
        }
        elements[size]=item;
    }

    public T pop(){
        if (isEmpty()){
            System.err.println("stack is empty ");
            return null;
        }
        return (T) elements[size--];
    }
    public boolean isEmpty(){
        return (size<0);
    }
    public T peek(){
        if (isEmpty()){
            System.err.println("EMPty");
        }
        return (T) elements[size];

    } 
    
}
