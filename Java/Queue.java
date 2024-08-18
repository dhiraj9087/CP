public class Queue<T> {
    private int front;
    private int rear;
    private int size;
    private static final int DEFAULT_CAPACITY = 10;
    private Object[] elements;

    

    public Queue(){
        elements = new Object[DEFAULT_CAPACITY];
        front = 0;
        rear  = -1;
        size = 0;
    }

    public void push(int item){
        if (size>=DEFAULT_CAPACITY){
            System.err.println("queue overflow");
            return;
        }
        rear = (rear+1)%DEFAULT_CAPACITY;
        elements[rear] = item;
        size++;
    }

    public T pop(){
        if (isEmpty()){
            System.err.println("queue empty");
            return null;
        }

        T item = (T) elements[front];
        elements[front]  = null;
        front = (front + 1) % DEFAULT_CAPACITY;
        size--;
        return item;


    }
    public boolean isEmpty(){
        return size == 0;
    }

    public T peek(){
        if (isEmpty()){
            System.err.println("queue empty ");
            return null;
        }
        return (T) elements[front];
    }

}
