import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        for(int i = 0; i < sizes.length; i++){
            if (sizes[i][0] < sizes[i][1]){
                int change = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = change;
            }
        }
        int max_x = 0;
        int max_y = 0;
        for (int i = 0; i < sizes.length; i++){
            if (max_x < sizes[i][0]){
                max_x = sizes[i][0];
            }
            if(max_y < sizes[i][1]){
                max_y = sizes[i][1];
            }
        }
        int answer = max_x * max_y;
        return answer;
    }
}