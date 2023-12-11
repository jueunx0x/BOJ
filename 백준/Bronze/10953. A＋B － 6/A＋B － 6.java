import java.io.*;

import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        StringTokenizer stz ;
        int T = sc.nextInt();
        int sum=0;
        for(int i=0;i<T;i++){
            String str = sc.next();
            stz = new StringTokenizer(str,",");

            int a = Integer.parseInt(stz.nextToken());
            int b = Integer.parseInt(stz.nextToken());
            sum = a+b;

            System.out.println(sum);
            sum = 0;
        }
        sc.close();
        // Press Ctrl+R or click the green arrow button in the gutter to run the code.
    }

}