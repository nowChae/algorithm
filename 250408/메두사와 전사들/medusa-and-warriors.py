from collections import deque

N, M = map(int, input().split(' '))
s_r, s_c, e_r, e_c = map(int, input().split(' '))
warriors = list(map(int, input().split(' ')))
village = [list(map(int, input().split(' '))) for _ in range(N)]

# # 2: 집, 3: 공원, 4: 전사들
# village[s_r][s_c] = 2
# village[e_r][e_c] = 3
# for i in range(len(warriors)//2):
#     village[i*2][i*2 - 1] = 4

#상 하 좌 우
direction = [0, 1, 2, 3]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#메두사 포지션
m_posi_r, m_posi_c = s_r, s_c
visited = {(m_posi_r, m_posi_c)}

# 도로는 0, 아니면 1
# 메두사는 최단경로로 도로만 따라서 공원으로 이동
# 전사는 어느칸이든 이동 가능 - 메두사를 향해

# 1. 메두사 이동 함수
# 범위 체크
# 도로인지 여부 판단
# 최단 경로로 (점점 목적지에 가까워지면 됨)
# 갈수 있는 방향 찾기

# 범위 체크 
def range_check(r, c):
    if 0 <= r and r < N and 0 <= c and c < N:
        return True
    return False 

# 도로 체크
def road_check(r, c):
    if village[r][c] == 0:
        return True
    return False

# 최단 거리로 메두사 이동 함수 
def dir_sec(r, c):
    # 둘다 맞지 않는 경우
    if r != e_r and c != e_c:
        # 목적지가 왼쪽 아래
        if r < e_r and c > e_c: 
            return [1, 2, 0, 3]
        # 목적지가 오른쪽 아래   
        elif r < e_r and c < e_c: 
            return [1, 3, 0, 2]
        # 목적지가 왼쪽 위
        elif r > e_r and c > e_c: 
            return [0, 2, 1, 3]
        # 목적지가 오른쪽 위
        elif r > e_r and c < e_c: 
            return [0, 3, 1, 2]

    # 같은 행인 경우
    elif r == e_r  and c != e_c:
        # 목적지가 왼쪽   
        if c > e_c:
            return [3, 0, 1, 2]
        # 목적지가 오른쪽
        elif c < e_c:
            return [2, 0, 1, 3]


    # 같은 열인 경우
    elif c == e_c and r != e_r:
        # 목적지가 아래
        if r < e_r:
            return [1, 2, 3, 0]
        # 목적지가 위
        elif r > e_r:
            return [0, 2, 3, 1]

    #둘 다 같은 경우 - 목적지 도착 
    else:
        return [0, 1, 2, 3]

def monster_move(r, c):
    move_sec = dir_sec(r, c)
    for m in move_sec:
        new_r = r + dr[m]
        new_c = c + dc[m]
        new_position = (new_r, new_c)
        print(new_position)
        if  range_check(new_r, new_c) and road_check(new_r,new_c) and (new_position not in visited):
            visited.add(new_position)
            r = new_r
            c = new_c
            break
    return (r, c)
    


print(m_posi_r, m_posi_c)
m_posi_r, m_posi_c = monster_move(m_posi_r, m_posi_c)
print(m_posi_r, m_posi_c)
m_posi_r, m_posi_c = monster_move(m_posi_r, m_posi_c)
print(m_posi_r, m_posi_c)

m_posi_r, m_posi_c = monster_move(m_posi_r, m_posi_c)
print(m_posi_r, m_posi_c)

m_posi_r, m_posi_c = monster_move(m_posi_r, m_posi_c)
print(m_posi_r, m_posi_c)

m_posi_r, m_posi_c = monster_move(m_posi_r, m_posi_c)




# 메두사 이동
# 도로를 따라서 한칸만 이동 - 공원으로
# 만약 이동한 공간에 전사가 있으면 전사 사라짐
# 상하좌우 우선순위 
# 도달 경로 없을 수 있음

# 2. 메두사 시선 함수
# 방향에 따라 전사를 가장 많이 볼 수 있는 것 택하기

# 시선에 걸리면 전사의 상태를 이동할 수 없도록 변경

# 메두사 시선
# 상하좌우 방향 선택해 바라봄
# 90도의 시야각
# 메두사에게 보이는 지 안보이는 지 판단
# 시야각 안에 있으면 움직일 수 없음
# 가장 많이 볼 수 있는 방향으로 봄

# 3. 전사 이동 함수
# 어디든 거리를 줄이는 방향으로 이동하는데, 시야 속에 들어가지 않도록 체크 후 가능


# 전사 이동
# 최대 두 칸 이동, 같은 칸 공유 가능
# 거리를 줄일 수 있는 방향으로 
# 상하좌우 우선순위
# 시야 X 인 곳으로 
# 한번 더 반복 

# 4. 전사 공격 함수
# 메두사와 위치가 같은 경우 - 전사 이동 함수에서 판단해야할 듯 싶음
# 공격횟수 늘리고 아예 사라짐 -> 0으로 변경하면 될 것 같음 (메두사는 도로에만 존재)


# 전사 공격
# 메두사와 같은 칸 - 공격하고 사라짐

# 전사가 이동한 거리의 합, 돌이 된 전사 수, 공격한 전사수 
# 메두사가 공원에 도착하면 0 출력
# 메두사 집에서 공원까지 못가면 -1 출력

##### 결과 
# 각 턴마다 결과를 리스트에 저장하고, 
# 만약 도착하면 결과들과 0을 마지막에 출력
# 도착하지 못하면 그냥 -1만 출력