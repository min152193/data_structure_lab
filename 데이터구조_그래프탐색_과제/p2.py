##
## TODO : 콘서트 공간에서 무대의 개수를 계산해 반환해주는 함수를 작성해주세요.

'''
2차원 배열 격자 안에서 서로 상하좌우로 연결된 빈 공간들의 덩어리 개수를 세는 문제이므로, 하나의 빈 공간에서 출발해 연결된 모든 빈 공간을 방문 처리하여 하나의 독립된 무대로 묶어주기 위해 BFS를 구성했습니다.

방문 여부를 기록할 2차원 리스트 visited를 생성한 뒤 격자의 모든 칸을 이중 반복문으로 순회하면서 무대공간임과 동시에 아직 방문하지 않은 칸을 발견하면 이를 새로운 무대의 시작점으로 판단하여 BFS 탐색을 진행합니다.
이후 상, 하, 좌, 우로 연결된 모든 0들을 Queue에 넣어 visited 처리했습니다.
하나의 BFS 탐색이 끝나면 연결된 한 덩어리의 무대 공간을 모두 찾은 것이 되기 때문에 answer를 1 증가시키는 로직으로 구성해봤습니다.

'''

import sys
import os
from collections import deque

## 입력 받는 코드입니다. 수정할 필요 없습니다.
sys.stdin = open('case.txt')
N, M = list(map(int, input().split()))
print(N, M)

concerts = []
for v in range(N):
    values = list(map(int, input().split()))
    concerts.append(values)


def count_stages(concerts):

    N = len(concerts) # 행의 개수
    M = len(concerts[0]) # 열의 개수
    
    # 방문 여부 체크용 격자 생성
    visited = [[False] * M for _ in range(N)] # N행 M열의 2차원 리스트로 False 초기화
    answer = 0 # 무대 공간의 개수
    
    # 상하좌우 맞닿은 네 방향 탐색을 위해 방향 벡터 생성
    dr = [-1, 1, 0, 0] # 행 이동
    dc = [0, 0, -1, 1] # 열 이동
    
    # 연결된 하나의 무대 공간을 전부 visited 처리하는 BFS
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True # 시작점 방문 true
        
        while queue:
            r, c = queue.popleft()
            
            # 현재 위치에서 상하좌우 탐색
            for i in range(4):
                nr = r + dr[i] # 다음 행 위치
                nc = c + dc[i] # 다음 열 위치
                
                # 격자 범위 벗어나는지 확인
                if 0 <= nr < N and 0 <= nc < M:
                    # 아직 미방문, 빈 공간(0)인 경우에만 이동
                    if not visited[nr][nc] and concerts[nr][nc] == 0: # 빈 공간인 경우(0인 경우)
                        visited[nr][nc] = True # 같은 무대 공간으로 묶기
                        queue.append((nr, nc)) # 다음 위치로 이동

    # 전체 콘서트장 격자 하나씩 돌기
    for r in range(N):
        for c in range(M):
            if concerts[r][c] == 0 and not visited[r][c]: # 빈 공간이면서, visited==false인 곳을 찾았을 때
                bfs(r, c)    # 그 칸과 연결된 모든 빈 칸을 true 처리
                answer += 1  # 새로운 무대 공간을 찾았으니 answer 개수 추가
                
    return answer

print(count_stages(concerts)) # 무대 개수 출력