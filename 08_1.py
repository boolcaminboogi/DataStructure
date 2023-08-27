#실습과제1

class Set :
    def __init__(self) :
        self.items=[]
    
    def size(self) :
        return len(self.items)
    def display(self, msg) :
        print(msg, self.items)
    def contains(self, items):
        return item in self.items

    #삽입연산
    def insert(self, elem) :		#정렬된 상태를 유지하면서 elem을 삽입
        if elem in self.items : return		#이미 있는경우
        for idx in range(len(self.itmes)) :	#loop : n번
            if elem<self.items[idx] :		# 삽입할 위치 idx를 찾음
                self.items.insert(idx, elem)	#그 위치에 삽입
                return
        self.items.append(elem)				#맨 뒤에 삽입
        
    #삭제연산
    def delete(self, elem) :
        if elem in self.items :
            self.items.remove(elem)
        
    #비교연산
    def __eq__(self, setB) :			#두 집합 self, setB가 같은 집합인가?
        if self.size !=setB.size() :	#원소의 개수가 같아야한다
            return False
        for idx in range(len(self.items)) :			#loop :n번
            if self.items[idx] !=setB.items[idx] :	#원소별로 같은지 검사
                return False
        return True

    #합집합
    def union(self, setB):		#o(mn)->o(n+m)
        newSet = Set()
        a = 0
        b = 0
        while a<len(self.items) and b<len(setB.items) :
            valueA=self.items[a]
            valueB=self.items[b]
            if valueA < valueB :
                newSet.items.append(valueA)
                a+=1
            elif valueA > valueB :
                newset.items.append(valueB)
                b+=1
            else :
                newSet.items.append(valueA)
                a+=1
                b+=1
        
        while a<len(self.items) :
            newSet.items.append(self.items[a])
            a+=1
            
        while b<len(setB.items) :
            newSet.items.append(setB.items[b])
            b+=1
            
        return newSet

    #교집합p7_3
    def intersect(self, setB) :		#o(mn)->o(n+m)
        newSet=Set()
        a=0
        b=0
        while a<len(self.items) and b<len(setB.items) :
            valueA = self.items[a]
            valueB = self.items[b]
            if valueA < valueB :
                a+=1
            elif valueA > valueB :
                b+=1
            else :
                newSet.items.append(valueA)
                a+=1
                b+=1
            
        return newSet

    #차집합
    def difference(self, setB): #p7_4
        newSet=Set()
        a=0
        b=0
        while a<len(self.itmes) and b<len(setB.items):
            valueA=self.items[a]
            valueB=setB.itmes[b]
            if valueA < valueB :
                newSet.items.append(valueA)
                a+=1
            elif valueA > valueB :
                b+=1
            else :
                a+=1
                b+=1
                
        while a<len(self.items) :
            newSet.items.append(self.items[a])
            a+=1
        
        return newSet
    


setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A : ')

setB = Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B : ')

setB.insert('빗')
setA.delete('손수건')
setA.display('Set A : ')
setB.display('Set B : ')

setA.union(setB).display('A U B : ')
setA.intersect(setB).display('A ^ B : ')
setA.different(setB).display('A - B : ')
