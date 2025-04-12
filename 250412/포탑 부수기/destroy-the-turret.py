from collections import deque
import math

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
attack_time = [[0] * M for _ in range(N)]
time = 1

# 방향 상수
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 좌표 변환 함수 (토러스 구조)
def position_change(r, c):
    return r % N, c % M

# 살아있는 포탑 목록 관리 (최초 한 번만 전체 순회)
alive_turrets = []
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            alive_turrets.append((i, j))

def weak_top():
    """가장 약한 포탑 선정 - 리스트 정렬 방식으로 최적화"""
    global time, alive_turrets
    
    # 살아있는 포탑만 정렬
    # 정렬 조건: 
    # 1. 공격력 오름차순
    # 2. 최근 공격 시간 내림차순
    # 3. 행+열 내림차순
    # 4. 열 내림차순
    weak_turrets = []
    for r, c in alive_turrets:
        if board[r][c] > 0:
            # 튜플 순서 유지: (공격력, 공격 시간, 행+열, 열, 행, 열)
            weak_turrets.append((board[r][c], attack_time[r][c], r+c, c, r, c))
    
    # 정확한 정렬 기준 적용
    weak_turrets.sort(key=lambda x: (x[0], -x[1], -(x[2]), -x[3]))
    
    if not weak_turrets:
        return (-1, -1)  # 예외 처리
    
    _, _, _, _, top_r, top_c = weak_turrets[0]
    board[top_r][top_c] += (N + M)
    attack_time[top_r][top_c] = time
    
    return (top_r, top_c)

def strong_top():
    """가장 강한 포탑 선정 - 리스트 정렬 방식으로 최적화"""
    # 살아있는 포탑만 정렬
    strong_turrets = [(board[r][c], attack_time[r][c], r+c, c, r, c) for r, c in alive_turrets if board[r][c] > 0]
    
    # 정렬 조건: 공격력 내림차순, 최근 공격 시간 오름차순, 행+열 오름차순, 열 오름차순
    strong_turrets.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    
    if not strong_turrets:
        return (-1, -1)  # 예외 처리
    
    _, _, _, _, top_r, top_c = strong_turrets[0]
    return (top_r, top_c)

def can_go(start, end):
    """BFS 최적화 - 큐 구조 및 방문 체크 개선"""
    if start == end:
        return (False, None)  # 시작점과 끝점이 같은 경우 처리
    
    board_path = [[(-1, -1)] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    # 큐에 시작 위치와 카운트를 함께 저장
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        cur_r, cur_c, cnt = queue.popleft()
        
        if cur_r == end[0] and cur_c == end[1]:
            return (True, board_path)
        
        for i in range(4):
            new_r, new_c = position_change(cur_r + dx[i], cur_c + dy[i])
            
            if board[new_r][new_c] > 0 and not visited[new_r][new_c]:
                queue.append((new_r, new_c, cnt + 1))
                visited[new_r][new_c] = True
                board_path[new_r][new_c] = (cur_r, cur_c)
    
    return (False, board_path)

def attack_1(start, end, board_path):
    """레이저 공격 - 관련된 포탑만 처리하도록 최적화"""
    relation_top = {start, end}
    
    attack_value = board[start[0]][start[1]]
    half_value = attack_value // 2
    
    board[end[0]][end[1]] -= attack_value
    
    # 경로 역추적
    cur_r, cur_c = end
    while True:
        cur_r, cur_c = board_path[cur_r][cur_c]
        if (cur_r, cur_c) == start:
            break
        relation_top.add((cur_r, cur_c))
        board[cur_r][cur_c] -= half_value
    
    return relation_top

def attack_2(start, end):
    """포탄 공격 - 원래 구현 방식 유지"""
    relation_top = {start, end}

    attack_value = board[start[0]][start[1]]
    half_value = attack_value // 2

    # 중요: 공격자의 공격 시간 업데이트
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

def broken_top():
    """부서진 포탑 처리 - 살아있는 포탑 목록 업데이트"""
    global alive_turrets
    
    # 포탑 목록 갱신
    new_alive = []
    for r, c in alive_turrets:
        if board[r][c] <= 0:
            board[r][c] = 0
        else:
            new_alive.append((r, c))
    
    alive_turrets = new_alive
    return len(alive_turrets)

def align(top_list):
    """포탑 정비 - 살아있는 포탑만 처리하도록 최적화"""
    for r, c in alive_turrets:
        if board[r][c] > 0 and (r, c) not in top_list:
            board[r][c] += 1

# 메인 로직
for _ in range(K):
    # 매 턴마다 살아있는 포탑 목록 갱신
    alive_turrets = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                alive_turrets.append((i, j))
                
    # 살아있는 포탑이 1개 이하라면 종료
    if len(alive_turrets) <= 1:
        break
        
    # 공격자 선정
    start = weak_top()
    if start == (-1, -1):
        break
    
    # 타겟 선정
    end = strong_top()
    if end == (-1, -1) or start == end:
        break
    
    # 공격 유형 선택
    state, board_path = can_go(start, end)
    if state:
        relation_top = attack_1(start, end, board_path)
    else:
        relation_top = attack_2(start, end)
    
    # 포탑 파괴 확인
    broken_top()
    alive_count = sum(1 for i in range(N) for j in range(M) if board[i][j] > 0)
    if alive_count <= 1:
        break
    
    # 포탑 정비
    align(relation_top)
    
    # 시간 증가
    time += 1

# 결과 출력
result = strong_top()
if result == (-1, -1):
    print(0)
else:
    print(board[result[0]][result[1]])