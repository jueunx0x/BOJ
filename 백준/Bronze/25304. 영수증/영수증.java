import java.util.Scanner;

import static java.lang.System.out;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        int count = sc.nextInt();
        int count_sum = 0;
        for (int i = 0; i < count; i++) {
            int money = sc.nextInt();
            int m_count = sc.nextInt();



            count_sum += (money*m_count);
          }
        if (sum == count_sum) {
            out.println("Yes");
        } else {
            System.out.println("No");
        }

    }
}