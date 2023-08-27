#def checkBrackets(statement):
#    stack = Stack()
#    for ch in statement:		#문자열의 각 문자에 대해
#        if ch in('{','[','('):
#            stack.push(ch)
#        elif ch in('}',']',')'):
#            if stack.isEmpty():
#                return False		#조건 2 위반
#            else:
#                left = stack.pop()
#                if(ch=="}" and left !="{") or \
#                  (ch=="]" and left !="[") or \
#                  (ch==")" and left !="("):
#                  return Fasle		#조건 3 위반
#    return stack.isEmpty()		#False이면 조건 1 위반
class Stack:
    def __init__(self):
        self.top=[]
    def isEmpty(self): return len(self.top)==0
    def size(self): return len(self.top)
    def clear(self): self.top=[]
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    #def peek(self):
    #    if not self.isEmpty():
    #        return self.top[-1]


def checkBracketsV2(lines):#예외처리 ",'가 나오면 flag를 꽂고 0,1 conversion을 하여 검사를 안하도록 한다.
    stack = Stack()
    conver=Stack()
    global lcnt, ccnt, eCode
    for line in lines:		#줄검사
        lcnt+=1
        for ch in line:		#단어검사
            ccnt+=1
        if ch in("\'","\""):
            a==0
            if ch in("/'", "\""):
                a==1
                if a==1:
                    if ch in('{','[','('):
                        stack.push(ch)
                    elif ch in('}',']',')'):
                        conver.pop()
                        if stack.isEmpty():
                            return 2 #False		#조건 2 위반
                        else:
                            left = stack.pop()
                            if(ch=="}" and left !="{") or \
                              (ch=="]" and left !="[") or \
                              (ch==")" and left !="("):
                              return 3 #False		#조건 3 위반                  
        if stack.isEmpty()==0:		#False이면 조건 1 위반
            return 1
        return 0

#filename="ArrayStack.h"
filename="brackettest.cpp"
infile=open(filename, "r")
lines= infile.readlines();
infile.close()

lcnt=0
ccnt=0
eCode=checkBracketsV2(lines)
print(filename, "--->", eCode)
print("라인 수 = ", lcnt)
print("문자 수 = ", ccnt)

