import java.io.*;

import java.util.Arrays;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        int[] arr = new int[T];
        for(int i =0;i<T;i++){
            arr[i] = sc.nextInt();
        }
        int min = arr[0];
        int max = arr[0];
        
        for(int i =0 ; i<arr.length ; i++){
            if(max<arr[i]){
                max = arr[i];
            }
            if(min>arr[i]){
                min = arr[i];
            }
        }
        System.out.print(min +" "+max);
        // Press Ctrl+R or click the green arrow button in the gutter to run the code.


    }

    }

