# DP 
# 배열을 사용한 동적 프로그래밍
# 배열을 사용해 모든 가능한 n에 대한 값을 저장 
# 배열을 사용하면 인덱스 접근이 빠르고, 공간 효율적임 

def make_one(n):
    # n일 때의 결과를 저장할 배열 
    memo = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # 현재 수에서 1을 빼는 경우를 우선 memo[현재수]에 넣어두고
        memo[i] = memo[i - 1] + 1

        # 현재 수가 2 또는 3으로 나누어 떨어지면 해당 연산을 고려
        if i % 2 == 0:
            # 위에서 계산한 memo[현재수] 와 memo[i // 2] + 1 중 더 작은 수를 memo[현재수]에 갱신
            memo[i] = min(memo[i], memo[i // 2] + 1)
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3] + 1)

    return memo[n] 

n = int(input())
print(make_one(n))