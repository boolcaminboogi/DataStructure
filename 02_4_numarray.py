n=int(input('숫자를 입력하세요 : '))
A=[]
A = list(range(1,n+1))

def printNum(n):  #순방향 나열
    print('나열')
    print(A)

def printRevNum(n):	#역방향 나열
    A.reverse()
    print('역순')
    print(A)
        
print(printNum(n))
print(printRevNum(n))