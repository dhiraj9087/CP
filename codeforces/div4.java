// package codeforces;

import java.util.Scanner;

/**
 * div4
 */
public class div4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-->0) {
            int a=sc.nextInt();
            int b=sc.nextInt();
            int c=sc.nextInt();
            if (a<b && b<c)
            {
                System.out.println("STAIR");

            }
            else if (a<b && b>c)
            {
                System.out.println("PEAK");

            }
            else System.out.println("NONE");
        
        }
        // return 0;
        
        sc.close();
    }
}