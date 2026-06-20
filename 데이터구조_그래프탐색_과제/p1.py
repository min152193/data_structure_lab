from collections import deque

A = {
    0: [1, 2, 3],
    1: [0, 2, 4, 5],
    2: [0, 1, 6],
    3: [0],
    4: [1],
    5: [1],
    6: [2]
}

def bfs(A):
    """
    deque를 이용한 BFS 탐색
    
    Args
        A (dict) - 노드 번호는 key, 인접 노드 리스트는 value
        
    Returns
        list - 0번 노드부터 시작하여 BFS로 탐색을 완료한 노드들의 순서 리스트
        
    Note
        - 파이썬의 deque를 활용하여 선입선출(FIFO) 구조의 큐를 구현했습니다.
        - 인접한 노드들을 차례대로 방문하면서 중복 방문을 막기 위해 set(visited)을 사용했습니다.
        - 같은 레벨의 노드들은 데이터에 정의된 순서(작은 번호 우선)대로 자연스럽게 탐색됩니다.
    """
    answer = []
    visited = set([0])  # 시작 노드 0 방문 처리
    queue = deque([0])  # deque 사용
    
    while queue:
        node = queue.popleft()
        answer.append(node)
        
        # 이웃 노드 순차 탐색
        for neighbor in A[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return answer

def dfs(A):
    """
     stack을 이용한 DFS 탐색
    
    Args
        A (dict) - 인접 리스트 형태로 표현된 그래프 데이터
        
    Returns
        list - 0번 노드부터 시작하여 DFS로 탐색을 완료한 노드들의 순서 리스트
        
    Note
        - 파이썬의 기본 list를 활용하여 후입선출 구조의 스택을 구현했습니다.
        - 동일 깊이일 때 번호가 작은 노드를 먼저 방문해야 하므로 인접 노드들을 스택에 넣을 때 reverse하여 넣어주었습니다.
          (가장 작은 번호가 스택의 맨 위에 올라오게 되어 우선탐색됨)
    """
    answer = []
    visited = set([0])  # 시작 노드 0 방문 처리
    stack = [0]         # 스택 사용(초기화)
    
    while stack:
        node = stack.pop()
        answer.append(node)
        
        # 인접 노드 순차 탐색 (번호 작은 노드 우선, 스택에 넣을 때 reverse)
        for neighbor in reversed(A[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                
    return answer

# 아래는 체크함수입니다. 수정하실 필요 없습니다.
bfs_result = bfs(A)
dfs_result = dfs(A)

assert bfs_result == [0,1,2,3,4,5,6]
assert dfs_result == [0,1,4,5,2,6,3]
print('PASSED!')