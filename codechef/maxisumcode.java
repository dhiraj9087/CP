import java.util.Scanner;

public class maxisumcode {
    static final long MOD = 1000000007L;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt(); // Number of test cases

        while (t-- > 0) {
            int n = scanner.nextInt(); // Size of the array
            int k = scanner.nextInt(); // Number of operations
            long[] a = new long[n];
            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextLong();
            }

            long maxSum = maxSubarraySum(a);
            long total = sumArray(a);

            if (maxSum <= 0) {
                System.out.println(total % MOD);
            } else {
                long ans = maxSum;
                long add = ans;
                while (k > 1) {
                    ans *= 2;
                    add += ans;
                    k--;
                }
                System.out.println((add + total) % MOD);
            }
        }
    }

    static long maxSubarraySum(long[] arr) {
        long maxSum = arr[0];
        long currentSum = arr[0];

        for (int i = 1; i < arr.length; i++) {
            currentSum = Math.max(arr[i], currentSum + arr[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }

    static long sumArray(long[] arr) {
        long sum = 0;
        for (long num : arr) {
            sum += num;
        }
        return sum;
    }
}
