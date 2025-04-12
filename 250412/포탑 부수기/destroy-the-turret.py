from collections import deque
import math

N, M, K = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]
attack_time = [[0] * M for _ in range(N)]
time = 1

alive_turrets = []
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            alive_turrets.append((i, j))


def weak_top():
    """가장 약한 포탑 선정 - 리스트 정렬 방식으로 최적화"""
    global time, alive_turrets

    # 살아있는 포탑만 정렬
    weak_turrets = [(board[r][c], attack_time[r][c], r + c, c, r, c) for r, c in alive_turrets if board[r][c] > 0]

    # 정렬 조건: 공격력 오름차순, 최근 공격 시간 내림차순, 행+열 내림차순, 열 내림차순
    weak_turrets.sort(key=lambda x: (x[0], -x[1], -x[2], -x[3]))

    if not weak_turrets:
        return (-1, -1)  # 예외 처리

    _, _, _, _, top_r, top_c = weak_turrets[0]
    board[top_r][top_c] += (N + M)
    attack_time[top_r][top_c] = time

    return (top_r, top_c)


def strong_top():
    """가장 강한 포탑 선정 - 리스트 정렬 방식으로 최적화"""
    # 살아있는 포탑만 정렬
    strong_turrets = [(board[r][c], attack_time[r][c], r + c, c, r, c) for r, c in alive_turrets if board[r][c] > 0]

    # 정렬 조건: 공격력 내림차순, 최근 공격 시간 오름차순, 행+열 오름차순, 열 오름차순
    strong_turrets.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))

    if not strong_turrets:
        return (-1, -1)  # 예외 처리

    _, _, _, _, top_r, top_c = strong_turrets[0]
    return (top_r, top_c)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


### 공격

def position_change(r, c):
    if r < 0:
        r = N - 1
    elif r >= N:
        r = 0

    if c < 0:
        c = M - 1
    elif c >= M:
        c = 0
    return (r, c)


# 경로 존재 여부 판단
def can_go(start, end):
    board_path = [[(-1, -1)] * M for _ in range(N)]

    visited = {start}
    queue = deque([start, 0])
    state = False

    while queue:
        cur_r, cur_c = queue.popleft()
        cnt = queue.popleft()

        if cur_r == end[0] and cur_c == end[1]:
            return (True, board_path)

        for i in range(4):
            new_r = cur_r + dx[i]
            new_c = cur_c + dy[i]
            new_r, new_c = position_change(new_r, new_c)

            if board[new_r][new_c] != 0 and (new_r, new_c) not in visited:
                queue.append((new_r, new_c))
                queue.append(cnt + 1)
                visited.add((new_r, new_c))
                board_path[new_r][new_c] = (cur_r, cur_c)

    return (state, board_path)


#### 레이저 공격
#### 경로가 존재할 경우
#### 최단 경로 공격 ( 우 하 좌 상 우선 순위)
#### 공격자는 공격력 만큼
#### 걸어온 경로는 절반 만큼 (공격력 // 2)
def attack_1(start, end, board_path):
    relation_top = {start, end}

    attack_value = board[start[0]][start[1]]
    half_value = attack_value // 2

    board[end[0]][end[1]] -= attack_value
    cur = board_path[end[0]][end[1]]
    c_r = cur[0]
    c_c = cur[1]

    while True:
        if c_r == start[0] and c_c == start[1]:
            break
        relation_top.add((c_r, c_c))
        board[c_r][c_c] -= half_value
        cur = board_path[c_r][c_c]
        c_r, c_c = cur[0], cur[1]

    return relation_top


#### 포탄 공격
#### 경로가 존재하지 않을 경우
#### 공격지에 포탄 떨구고
#### 그 주변 8개에 절반 만큼 피해 (공격력 // 2)

def attack_2(start, end):
    relation_top = {start, end}

    attack_value = board[start[0]][start[1]]
    half_value = attack_value // 2

    attack_time[start[0]][start[1]] = time

    for i in range(end[0] - 1, end[0] + 2):
        for j in range(end[1] - 1, end[1] + 2):
            r, c = position_change(i, j)
            if board[r][c] != 0:
                relation_top.add((r, c))
                if r == end[0] and c == end[1]:
                    board[r][c] -= attack_value
                else:
                    board[r][c] -= half_value

    return relation_top


### 포탑 부서짐
#### 0 이하 되면 부서짐
def broken_top():
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] <= 0:
                board[i][j] = 0
                zero_cnt += 1
    return zero_cnt


### 포탑 정비
#### 무관 포탑 공격력 + 1
def align(top_list):
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and (i, j) not in top_list:
                board[i][j] += 1


# K번 반복
# 부서지지 않은 포탑이 1개가 되면 중지

for _ in range(K):
    start = weak_top()
    end = strong_top()
    ## 공격 유형 선택해야함
    # 경로가 존재하면
    relation_top = {}
    state, board_path = can_go(start, end)
    if state:
        relation_top = attack_1(start, end, board_path)
    else:
        relation_top = attack_2(start, end)

    zero_cnt = broken_top()
    if (N * M) - zero_cnt <= 1:
        break
    align(relation_top)

result_strong = strong_top()
print(board[result_strong[0]][result_strong[1]])
