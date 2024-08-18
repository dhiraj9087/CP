import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Cp{
    static Scanner sc = new Scanner(System.in);
    // static boolean[] sieveOfEratosthenes(int limit){
    //     boolean isprime[] = new boolean[limit+1];
    //     Arrays.fill(isprime, true);
    //     isprime[0]=false;
    //     isprime[1]=false;
    //     for (int i=2;i<=Math.sqrt(limit);i++){
    //         if (isprime[i]){
    //             for (int j=i*i;j<=limit;j+=i){
    //                 isprime[j]=false;
    //             }
    //         }
    //     }
    //     return isprime;
    // }

    
    
    static void main() throws IOException{
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        sc.nextLine();
        String s = sc.nextLine();
        long[] pre = new long[n];
        pre[0] = a[0];
        for(int i=1;i<n;i++){
            pre[i] = pre[i-1]+a[i];
        }
        int l=0;
        int r=n-1;
        long ans=0;
        while (l<r){
            if (s.charAt(l)=='L' && s.charAt(r)=='R'){
                if (l==0){
                    ans += pre[r];
                }
                else{
                    ans += (pre[r]-pre[l-1]);
                }
                l++;
                r--;
            }
            else if(s.charAt(l)=='L' && s.charAt(r)=='L'){
                r--;
            }
            else if(s.charAt(l)=='R' && s.charAt(r)=='R'){
                l++;
            }
            else{
                l++;
                r--;
            }

        }
        System.out.println(ans);
        // for (int i:pre){
        //     System.out.println(i);
        // }
    }
  
    public static void main (String[] args) throws java.lang.Exception{

        // Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        // boolean[] arr = sieveOfEratosthenes(201);
        while (t-->0)
        {
            main();

        }
        sc.close();
    }
}
