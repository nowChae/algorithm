
import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] student = new int[n + 1];
        Arrays.fill(student, 1); 


        for (int l : lost) {
            student[l]--; 
        }

        for (int r : reserve) {
            student[r]++; 
        }

        for (int i = 1; i <= n; i++) {
            if (student[i] == 0) { 
                if (i - 1 >= 1 && student[i - 1] == 2) {  
                    student[i - 1]--;
                    student[i]++;
                } else if (i + 1 <= n && student[i + 1] == 2) { 
                    student[i + 1]--;
                    student[i]++;
                }
            }
        }

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (student[i] > 0) { 
                answer++;
            }
        }

        return answer;
    }
}
