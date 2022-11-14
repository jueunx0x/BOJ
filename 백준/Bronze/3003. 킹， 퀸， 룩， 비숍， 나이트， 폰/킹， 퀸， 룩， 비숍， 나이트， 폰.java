import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int pin[]={1,1,2,2,2,8};
        int input[]=new int[6];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i<pin.length; i++) {
            input[i] = sc.nextInt();
        }
        for (int i=0;i<pin.length; i++){
            System.out.printf(String.valueOf(pin[i]-input[i])+" ");
        }
    }
}