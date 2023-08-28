import java.io.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int T =sc.nextInt();
        sc.close();
        // Press Ctrl+R or click the green arrow button in the gutter to run the code.
        for ( int i = 1 ; i <= T ; i++ ){
            for( int j = 1 ; j <= T-i ; j++ ) {
                System.out.print(" ");
            }
            for( int k = 1 ; k <= i ; k++ ){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
