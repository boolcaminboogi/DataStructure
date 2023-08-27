#힙 사용
import heapq

parent=[]		#각 노드의 부모노드 인덱스
set_size=0		#전체 집합의 개수

def Clear_set(nSets):
    global set_seize, parent
    set_Size = nSets
    for i in range(nSets):
        parent.append(-1)

def init_set(nSets):
    global set_seize, parent
    set_Size = nSets
    for i in range(nSets):
        parent.append(-1)
        
def find(id):
    while(parent[id] >=0):
        id = parent[id]
    return id;

def union(s1, s2):
    global set_size
    parent[s1] = s2
    set_size = set_size-1
    
def MSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []
    w_sum=0
    heapq.heapify(eList)
    
    for i in range(vsize-1):
        for j in range(i+1, vsize):
            if adj[i][j] != None:
                heapq.heappush(adj[i][j],(i,j))	#힙

                
    #간선 리스트를 가중치의 내림차순으로 정렬 : 람다 함수 사용
    eList.sort(key=lambda e : e[2], reverse = True)
    
    edgeAccepted = 0
    while(edgeAccepted < vsize-1):
        e = heapq.heappop(-1)		#힙
        uset=find(e[0])
        vset=find(e[1])
        
        if uset!=vset:
            print("간선 추가 : (%s, %s, %d)"%(vertex[e[0]], vertex[e[1]], e[2])) #가중치의 합 추가
            w_sum +=e[2]
            union(uset, vset)
            edgeAccepted+=1
    Clear_set()        
            
            
vertex = ['A',		'B',		'C',		'D',		'E',		'F',		'G']
weight = [[None,	29,			None,		None,		None,		10,			None],
          [29,		None,		16,			None,		None,		None,		15],
          [None,	16,			None,		12,			None,		None,		None],
          [None,	None,		12,			None,		22,			None,		18],
          [None,	None,		None,		22,			None,		27,			25],
          [10,		None,		None,		None,		27,			None,		None],
          [None,	15,			None,		18,			25,			None,		None]]


print("MST By Kruskal's Algorithm")
w_MST = MSTKruskal(vertex, weight)
print("Sum MST Weights : ", w_MST)



