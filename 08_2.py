#엔트리 객
class Entry :
    def __init__(self, key, value) :
        self.key = key
        self.value=value
        
    def __str__(self) :
        return str("%s%s"%(self.key, self.value))

#체이닝을 이용한 해시 
class HashChainMap :
    def __init__(self,M) :
        self.table=[None]*M
        self.M=M
        
    def hashFn(self, key) :
        sum=0
        for c in key :
            sum=sum+ord(c)
            return sum%self.M
    
    def insert(self,key,value) :
        idx = self.hashFn(key)
        self.table[idx]=Node(Entry(key,value),self.table[idx])
        entry=Entry(key,value)
        node=Node(entry)
        node.link=self.table[idx]
        self.table[idx]=node
    
    def search(self,key):
        idx=self.hashFn(key)
        node=self.table[edx]
        while node is not None:
            if node.data.key ==key:
                return node.data
            node=node.link
        return None
    
    def delete(self, key) :
        idx = self.hashFn(key)
        node = self.table[idx]
        before=None
        while node is not None:
            if node.data.key==key:
                if before==None:
                    self.table[idx]=node.link
                else :
                    before.link=node.link
                return
            before=node
            node=node.link
            
    def display(self,msg):
        print(msg)
        for idx in range(len(self.table)) :
            node = self.table[idx]
            if node is not None :
                print("[%2d] -> "%idx, end='')
                while node in not None:
                    print(node.data, end=' -> ')
                    node = node.link
                print()

###########################################################################
#선형조사를 이용한 해시
class LinearProbMap :
    def hashFn(self, key) :
        sum=0
        for c in key : sum=sum+ord(c)
        return sum%self.M

    def insert(self, key, value) :
        id = self.hashFn(key)
        count = self.M
        while count>0 and (self.table[id] != None and self.table[id] !=-1) :
            id = (id+1+self.M)%self.M
            count-=1
            
        if count>0 :
            self.table[id] = Entry(key, value)
        return

    def search(self, key):
        id =self.hashFn(key)
        count = self.M
        while count>0:
            if self.table[id]==None : return None
            if self.table[id]!=-1 and self.table[id].key==key:
                return self.table[id]
            id = (id+1+self.M)%self.M
            count-=1
        return None

    def delete(self,key) :
        id=self.hashFn(key)
        count = self.M
        while count>0 :
            if self.table[id]==None : return None
            if self.table[id] != -1 and self.table[id].key ==key :
                self.table[id] = -1
                return
            id=(id+1+self.M)%self.M
            count-=1
            
    def display(self, msg) :
        print(msg)
        for idx in range(len(self.table)) :
            none=self.table[idx]
            print("[%2d] -> "%idx, self.table[idx])
            
##########################################################################            
            
#순차탐색 맵    
class SequentialMap :
    def __init__(self) :
        self.table = []		#맵의 레코드 테이블
    
    def size(self): return len(self.table)		#레코드의 개수
    def display(self, msg) :					#보기 좋게 출력
        print(msg)
        for entry in self.table :				#테이블의 모든 엔트리에 대해
            print(" ", entry)					#출력(연산자 중복함수 사용)
            
    def insert(self, key, value) :		#삽입연산
        self.table.append(Entry(key, value))	#리스트 맨 뒤에 추가
        
    def search(self, key) :		#순차 탐색 연산
        pos=sequential_search(self.table, key, 0, self.size()-1)
        if pos is not None : return self.table[pos]
        else : return None
        
    def delete(self, key) :		#삭제 연산 : 항목 위치를 찾아 pop
        for i in range(self.size()):
            if self.table[i].key==key:		#삭제할 위치를 먼저 찾고
                self.table.pop(i)			#리스트의 pop으로 삭제
                return

            
#테스트 코드
#삽입
map = LinearProbMap()
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형탐색')
map.insert('game', '게임')
map.insert('binary search', '이진탐색')
map.display("나의 해싱단어장 : ")

#탐색
print("탐색 : game --> ", map.search('game'))
print("탐색 : over --> ", map.search('over'))
print("탐색 : data --> ", map.search('data'))

#삭제
map.delete('game')
map.display("나의 해싱 단어장")
print("탐색 : game --> ", map.search('game'))

