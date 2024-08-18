import java.util.Scanner;

public class userinput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num = sc.nextLine();
        // sc.nextLine();
        int num3 = sc.nextInt();
        // sc.nextLine();
        long num4 = sc.nextLong();
        double num5  = sc.nextDouble();
        System.out.println(num);
        System.out.println(num3);
        System.out.println(num4);
        System.out.println(num5);
        sc.close();

        
    }
}
