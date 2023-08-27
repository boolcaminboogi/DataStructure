import collections as cols			#큐로 할것
#큐 클래스


#인접행렬
vertex = 	['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [	[0,	1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 0]]


def dfs_recur(adjMat, vertex, visited, id):
    print(vertex[id], end='')		#현재 검사하고 정점을 출력
    visited[id] = True				#현재 정점을 방문한 것으로 기록
    for v in range(len(vertex)):	#반복실행 => 현재 정점의 모든 행(모든 정점,인덱스)에 대해서
        if visited[v] == False and adjMat[id][v] ==1:		#만약 v번째 정점이 방문하지 않은 정점이며, 간선으로 연결되어
            dfs_recur(adjMat, vertex, visited, v)		#그 정점에 대해 순환 호출


def dfs(adjMat, vertex, start):
    visited = [False]*len(vertex)				#비어있는 리스트 : 방문한 정점을 기록하기 위한 리스트(초기화)
    dfs_recur(adjMat, vertex, visited, start)	#깊이우선 탐색 함수 호출)
    
            
from queue import Queue
def bfs(adjMat, vertex, start):
    visited = [False]*len(vertex)					#비어있는 리스트 : 방문한 정점을 기록하기 위한 리스트(초기화 전부 false)
    queue =cols.deque([start])						#큐 객체 생성//컬렉션 덱 객체 생성(큐로 사용)
    #큐에 현재 정점 삽입
    #현재 정점 방문한 것으로 기록
    while queue:										#반복실행->조건 : 큐가 비어있지 않다면
        vertex = queue.popleft()						#큐에서 데이터(정점)를 하나 빼냄
        print(vertex, end='')							#큐에서 빼낸 데이터(정점)을 출력
        for v in range(len(vertex)):						#반복실행 => 현재 정점의 모든 행(모든 정점,인덱스)에 대해서
            if visited[v] == False and adjMat[id][v] ==1:		#만약 v번째 정점이 방문하지 않은 정점이며, 간선으로 연결되어 있는 정점이라면
                queue.append(v)								#큐에서 v번째 정점을 삽입
                visited[v] = True                                            #v번째 정점 방문한 것으로 기록(add함수 사용x)
        

    #비어있는 리스트 : 방문한 정점을 기록하기 위한 리스트(초기화 전부 false)
    #큐 객체 생성
    #큐에 현재 정점 삽입
    #현재 정점 방문한 것으로 기록
    #반복실행->조건 : 큐가 비어있지 않다면
        #큐에서 데이터(정점)를 하나 빼냄
        #쿠에서 빼낸 데이터(정점)을 출력
        #반복 실행 => 현재 정점의 모든행(모든 정점,인덱스)에 대해서
                #만약 v번째 정점이 방문하지 않은 정점이며, 간선으로 연결되어 있는 정점이라면
                #큐에서 v번째 정점을 삽입
                #큐에 v번째 정점 방문한 것으로 기록
            

def st_dfs(adjMat, vertex, start):
    visited = [False]*len(vertex)				#비어있는 리스트 : 방문한 정점을 기록하기 위한 리스트(초기화)
    queue =cols.deque([start])						#큐 객체 생성//컬렉션 덱 객체 생성(큐로 사용)
    print(vertex[id], end='')		#현재 검사하고 정점을 출력
    visited[id] = True				#현재 정점을 방문한 것으로 기록
    for v in range(len(vertex)):	#반복실행 => 현재 정점의 모든 행(모든 정점,인덱스)에 대해서
        if visited[v] == False and adjMat[id][v] ==1:		#만약 v번째 정점이 방문하지 않은 정점이며, 간선으로 연결되어
            dfs_recur(adjMat, vertex, visited, v)		#그 정점에 대해 순환 호출


            
            
print('DFS : ', end="")
dfs(adjMat, vertex, 0)
print()

print('BFS : ', end="")
bfs(adjMat, vertex, 0)
print()

print('Spanning Tree(DFS) : ', end="")
st_dfs(adjMat, vertex, 0)
print()
            

        