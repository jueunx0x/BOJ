import java.io.*;

import java.io.BufferedWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        // Press Ctrl+R or click the green arrow button in the gutter to run the code.
        for (int i = 1; i <= T; i++) {

            // Press Ctrl+D to start debugging your code. We have set one breakpoint
            // for you, but you can always add more by pressing Cmd+F8.
            st = new StringTokenizer(br.readLine()," ");
            System.out.println("Case #" + i + ": "
                    +(Integer.parseInt(st.nextToken())
                    +Integer.parseInt(st.nextToken())));
        }
        bw.close();
    }
}