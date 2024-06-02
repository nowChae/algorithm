import java.io.*;
import java.util.*;

public class baekjoon15665 {
    static int N, M;
    static int[] nList; // 중복 제거한 숫자를 저장한 배열
    static List<Integer> result = new ArrayList<>(); // 숫자 조합을 임시로 저장하는 리스트
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer NM = new StringTokenizer(br.readLine()); // 한줄을 입력받아서 문자를 쪼개주는 도구
        N = Integer.parseInt(NM.nextToken()); //위에서 읽어온 N, M 값을 숫자로 변환
        M = Integer.parseInt(NM.nextToken());

        // 중복을 제거하고 배열에 넣기 
        Set<Integer> nSet = new HashSet<>(); // 중복을 자동으로 제거해줌 
        StringTokenizer numbers = new StringTokenizer(br.readLine()); // 한줄을 입력받아서 문자를 쪼개주는 도구 
        for (int i = 0; i < N; i++) { // N개 만큼 한줄에 입력되니 N개만큼 반복
            nSet.add(Integer.parseInt(numbers.nextToken())); //nSet에 숫자로 변환한 값을 넣음
        }

        nList = new int[nSet.size()]; // 중복이 정리된 선택할 수 있는 숫자 리스트 생성
        int index = 0;
        for (int num : nSet) {
            nList[index++] = num;
        }

        Arrays.sort(nList); // 정렬

        dfs();

        bw.flush();
        bw.close();
        br.close();
    }

    private static void dfs() throws IOException {
        if (result.size() == M) { // 길이가 M개가 되면 
            for (int num : result) {
                bw.write(num + " "); // 한 줄로 출력 
            }
            bw.newLine(); // 디음줄로 
            return;
        }

        for (int n : nList){ // 작은 값 부터 넣기 
            result.add(n);
            dfs();
            result.remove(result.size() - 1); // 마지막 값 빼기 
        }

    }
}
