import sys
input = sys.stdin.readline

N, K = map(int, input().split())

things = []
for _ in range(N):
    things.append(list(map(int, input().split())))

# dp[i]는 무게 i까지의 최대 가치를 저장
dp = [0] * (K + 1)

for i in range(N):
    weight, value = things[i]
    # 뒤에서부터 앞으로 순회하는 이유는 같은 i번째 물건이 중복 사용되지 않도록 하기 위함
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[K])
