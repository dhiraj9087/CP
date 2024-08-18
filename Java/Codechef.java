import java.util.*;
import java.io.*;

class Codechef{
    static Scanner sc = new Scanner(System.in);
    static boolean[] sieveOfEratosthenes(int limit){
        boolean isprime[] = new boolean[limit+1];
        Arrays.fill(isprime, true);
        isprime[0]=false;
        isprime[1]=false;
        for (int i=2;i<=Math.sqrt(limit);i++){
            if (isprime[i]){
                for (int j=i*i;j<=limit;j+=i){
                    isprime[j]=false;
                }
            }
        }
        return isprime;
    }

    
    
    static void main() throws IOException{
        int n = sc.nextInt();
        int k = sc.nextInt();
        int a[] = new int[n];
        
        
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
            if (!map.containsKey(a[i])){
                map.put(a[i],i);
            }
        }
        if (n==k){
            int sum = Arrays.stream(a).sum();
            System.out.println(2*sum-a[0]-a[n-1]);
            return;
        }
        int maxi=0;
        for (int i=1;i<51;i++){
            if (!map.containsKey(i)){
                continue;
            }
            int ind = map.get(i);
            PriorityQueue <Integer> pq = new PriorityQueue<>(Comparator.naturalOrder());
            int sum=0;
            for(int j=ind+1;j<n;j++){
                if(pq.size()==(k-2)){
                    maxi = Math.max(maxi,i+a[j]+sum);
                }
                pq.add(a[j]);
                sum += 2*a[j];
                if (pq.size() > (k-2)){
                    sum -= 2*pq.poll();
                }
            }
        }   
        System.out.println(maxi);
    }
  
    public static void main (String[] args) throws java.lang.Exception{

        // Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        // boolean[] arr = sieveOfEratosthenes(201);
        while (t-->0)
        {
            main();

        }
    }
}
