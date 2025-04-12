from collections import deque

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
attack_time = [[0] * M for _ in range(N)]  # 공격 시간 기록
time = 1

# 방향 상수
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 순서 (BFS 우선순위 방향)
dy = [1, 0, -1, 0]
dx2 = [0, 0, 0, -1, -1, -1, 1, 1, 1]  # 포탄 공격 9방향
dy2 = [0, -1, 1, 0, -1, 1, 0, -1, 1]

# 공격 참여 여부 추적
is_active = [[False] * M for _ in range(N)]

# 포탑 클래스 정의
class Turret:
    def __init__(self, x, y, attack_time, power):
        self.x = x
        self.y = y
        self.attack_time = attack_time
        self.power = power

# 턴 초기화 함수
def init_turn():
    global time
    for i in range(N):
        for j in range(M):
            is_active[i][j] = False
    time += 1

# 약한 포탑 선정 및 강화
def awake(live_turrets):
    # 포탑 정렬: 공격력 오름차순, 공격시간 내림차순, 행+열 내림차순, 열 내림차순
    live_turrets.sort(key=lambda t: (t.power, -t.attack_time, -(t.x + t.y), -t.y))
    
    # 가장 약한 포탑 선택 및 강화
    weak_turret = live_turrets[0]
    x, y = weak_turret.x, weak_turret.y
    
    board[x][y] += (N + M)  # 공격력 증가
    attack_time[x][y] = time  # 공격 시간 갱신
    weak_turret.power = board[x][y]  # 객체 정보 갱신
    weak_turret.attack_time = time
    is_active[x][y] = True  # 공격 참여 표시
    
    return weak_turret

# 레이저 공격
def laser_attack(weak_turret, strong_turret):
    sx, sy = weak_turret.x, weak_turret.y
    ex, ey = strong_turret.x, strong_turret.y
    power = weak_turret.power
    
    # BFS 경로 탐색을 위한 초기화
    visited = [[False] * M for _ in range(N)]
    back_x = [[-1] * M for _ in range(N)]
    back_y = [[-1] * M for _ in range(N)]
    
    # BFS 시작
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    can_attack = False
    
    while queue:
        x, y = queue.popleft()
        
        if x == ex and y == ey:
            can_attack = True
            break
        
        # 우, 하, 좌, 상 순서로 탐색 (우선순위 방향)
        for i in range(4):
            nx, ny = (x + dx[i]) % N, (y + dy[i]) % M
            
            # 이미 방문했거나 부서진 포탑은 건너뜀
            if visited[nx][ny] or board[nx][ny] == 0:
                continue
            
            visited[nx][ny] = True
            back_x[nx][ny] = x
            back_y[nx][ny] = y
            queue.append((nx, ny))
    
    # 공격 가능한 경우 데미지 적용
    if can_attack:
        # 가장 강한 포탑에 공격력만큼 데미지
        board[ex][ey] -= power
        if board[ex][ey] < 0:
            board[ex][ey] = 0
        is_active[ex][ey] = True
        
        # 경로 역추적하여 경로상 포탑에 절반 데미지
        cx, cy = back_x[ex][ey], back_y[ex][ey]
        while not (cx == sx and cy == sy):
            board[cx][cy] -= power // 2
            if board[cx][cy] < 0:
                board[cx][cy] = 0
            is_active[cx][cy] = True
            
            nx, ny = back_x[cx][cy], back_y[cx][cy]
            cx, cy = nx, ny
    
    return can_attack

# 포탄 공격
def bomb_attack(weak_turret, strong_turret):
    sx, sy = weak_turret.x, weak_turret.y
    ex, ey = strong_turret.x, strong_turret.y
    power = weak_turret.power
    
    # 타겟 포탑과 주변 8개 방향 포탑 공격
    for i in range(9):
        nx, ny = (ex + dx2[i]) % N, (ey + dy2[i]) % M
        
        # 공격자 자신은 공격하지 않음
        if nx == sx and ny == sy:
            continue
        
        # 이미 부서진 포탑은 건너뜀
        if board[nx][ny] == 0:
            continue
        
        # 타겟 포탑은 공격력 전체, 나머지는 절반 데미지
        if nx == ex and ny == ey:
            board[nx][ny] -= power
        else:
            board[nx][ny] -= power // 2
            
        # 포탑 파괴 확인
        if board[nx][ny] < 0:
            board[nx][ny] = 0
            
        # 공격 참여 표시
        is_active[nx][ny] = True

# 포탑 정비
def repair():
    for i in range(N):
        for j in range(M):
            # 공격에 참여하지 않은 살아있는 포탑은 공격력 +1
            if not is_active[i][j] and board[i][j] > 0:
                board[i][j] += 1

# 메인 로직
for _ in range(K):
    # 살아있는 포탑 목록 갱신
    live_turrets = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                live_turrets.append(Turret(i, j, attack_time[i][j], board[i][j]))
    
    # 포탑이 1개 이하면 종료
    if len(live_turrets) <= 1:
        break
    
    # 턴 초기화
    init_turn()
    
    # 약한 포탑 강화
    weak_turret = awake(live_turrets)
    
    # 가장 강한 포탑 선택 (power 내림차순, attack_time 오름차순, 행+열 오름차순, 열 오름차순)
    live_turrets.sort(key=lambda t: (-t.power, t.attack_time, t.x + t.y, t.y))
    strong_turret = live_turrets[0]
    
    # 레이저 공격 시도
    is_success = laser_attack(weak_turret, strong_turret)
    
    # 레이저 공격 실패 시 포탄 공격
    if not is_success:
        bomb_attack(weak_turret, strong_turret)
    
    # 포탑 정비
    repair()

# 가장 강한 포탑의 공격력 출력
max_power = 0
for i in range(N):
    for j in range(M):
        max_power = max(max_power, board[i][j])

print(max_power)