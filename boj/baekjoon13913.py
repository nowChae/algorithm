import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())
visited = [-1]*100001
path = []
def bfs(n, k):
    queue = deque([n,0])

    while queue:
        dn = queue.popleft()
        dt = queue.popleft()
        if dn == k:
            idx = dn
            while idx != n:
                path.append(idx)
                idx = visited[idx]
            path.append(n)
            return dt
        if dn - 1 > -1 and  visited[dn-1] == -1:
            queue.append(dn-1)
            queue.append(dt+1)
            visited[dn-1] = dn
        if dn + 1 < 100001 and  visited[dn+1] == -1:
            queue.append(dn+1)
            queue.append(dt+1)
            visited[dn+1] = dn
        if dn*2  < 100001 and visited[dn*2] == -1:
            queue.append(dn*2)
            queue.append(dt+1)
            visited[dn*2] = dn
print(bfs(N, K))
print(' '.join(map(str, path[::-1])))
    