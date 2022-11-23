import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int A=0,B=0,C=0,money=0;
        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();

        if(A==B && B==C){
            money=10000+A*1000;
        }
        else if(A==B || B==C){
            money = 1000+B*100;
        }
        else if(A==C){
            money = 1000+A*100;
        }
        else {
            money=Math.max(Math.max(A,B),C)*100;
        }
        System.out.println(money);
    }
}