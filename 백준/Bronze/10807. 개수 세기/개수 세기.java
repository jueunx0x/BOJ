import java.io.*;

import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] arr = new int[T];
        int sum=0;
        for(int i =0;i<T;i++){
            arr[i] = sc.nextInt();
        }
        int v = sc.nextInt();

        for(int i =0 ; i<arr.length; i++){
            if(v==arr[i]){
                sum+=1;
            }
        }
        System.out.println(sum);
        // Press Ctrl+R or click the green arrow button in the gutter to run the code.


    }

    }

