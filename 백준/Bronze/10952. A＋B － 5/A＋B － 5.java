import java.io.*;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int A,B;
        A=sc.nextInt();
        B=sc.nextInt();

        // Press Ctrl+R or click the green arrow button in the gutter to run the code.
        while (A!=0 && B!=0){
            System.out.println(A+B);
            A = sc.nextInt();
            B = sc.nextInt();
        }
    }
}
