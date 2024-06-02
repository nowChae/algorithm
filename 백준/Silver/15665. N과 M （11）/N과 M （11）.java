import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] nList;
    static List<Integer> result = new ArrayList<>();
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer NM = new StringTokenizer(br.readLine());
        N = Integer.parseInt(NM.nextToken());
        M = Integer.parseInt(NM.nextToken());

        Set<Integer> nSet = new HashSet<>();
        StringTokenizer numbers = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nSet.add(Integer.parseInt(numbers.nextToken()));
        }

        nList = new int[nSet.size()];
        int index = 0;
        for (int num : nSet) {
            nList[index++] = num;
        }

        Arrays.sort(nList);

        dfs();

        bw.flush();
        bw.close();
        br.close();
    }

    private static void dfs() throws IOException {
        if (result.size() == M) {
            for (int num : result) {
                bw.write(num + " ");
            }
            bw.newLine();
            return;
        }

        for (int i = 0; i < nList.length; i++) {
            result.add(nList[i]);
            dfs();
            result.remove(result.size() - 1);
        }
    }
}
