
parent=[]		#각 노드의 부모노드 인덱스
set_size=0		#전체 집합의 개수

def Clear_set(nSets):
    global set_seize, parent
    parent=[]
    set_size= 0

def init_set(nSets):
    global set_size, parent
    set_size = nSets
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
    
def MSTKruskal(vertex, adj, updown):	#파라매터 하나 추가(내림차순이냐 오름차순이냐(최소냐 최대냐)
    vsize = len(vertex)
    init_set(vsize)
    eList = []
    w_sum=0
    
    for i in range(vsize-1):
        for j in range(i+1, vsize):
            if adj[i][j] != None:
                eList.append((i,j,adj[i][j]))
                
    if updown == 1:
        #간선 리스트를 가중치의 내림차순으로 정렬 : 람다 함수 사용
        eList.sort(key=lambda e : e[2], reverse = True)
    
        edgeAccepted = 0
        while(edgeAccepted < vsize-1):
            e = eList.pop(-1)
            uset=find(e[0])
            vset=find(e[1])
        
            if uset!=vset:
                print("간선 추가 : (%s, %s, %d)"%(vertex[e[0]], vertex[e[1]], e[2])) #가중치의 합 추가
                w_sum +=e[2]
                union(uset, vset)
                edgeAccepted+=1
        
        return w_sum
        Clear_set()
                
    if updown == 0:
        #간선 리스트를 가중치의 오름차순으로 정렬 : 람다 함수 사용
        eList.sort(key=lambda e : e[2])
        
        edgeAccepted = 0
        while(edgeAccepted < vsize-1):
            e = eList.pop(-1)
            uset=find(e[0])
            vset=find(e[1])
            
            if uset!=vset:
                print("간선 추가 : (%s, %s, %d)"%(vertex[e[0]], vertex[e[1]], e[2])) #가중치의 합 추가
                w_sum +=e[2]
                union(uset, vset)
                edgeAccepted+=1
        
        return w_sum
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
print("MinST 가중치의 합 = ", MSTKruskal(vertex, weight, True))#내림차순
print("MaxST 가중치의 합 = ", MSTKruskal(vertex, weight, False))#오름차순











