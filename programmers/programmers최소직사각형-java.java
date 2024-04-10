import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        // 배열 요소의 크기 정렬
        sortSizes(sizes);

        // 최대 너비와 최대 높이 계산
        int maxWidth = 0;
        int maxHeight = 0;

        for (int[] size : sizes) {
            if (size[0] > maxWidth) {
                maxWidth = size[0];
            }
            if (size[1] > maxHeight) {
                maxHeight = size[1];
            }
        }

        // 최대 너비와 최대 높이를 곱하여 면적 계산
        return maxWidth * maxHeight;
    }
    
    // 배열 요소의 크기를 정렬하는 메소드
    private void sortSizes(int[][] sizes) {
        for (int[] size : sizes) {
            if (size[0] < size[1]) {
                swapDimensions(size);
            }
        }
    }

    // 크기를 바꾸는 메소드
    private void swapDimensions(int[] size) {
        int temp = size[0];
        size[0] = size[1];
        size[1] = temp;
    }
}
