class Polynomial:
    def __init__(self):		#생성자
        self.coef=[]		#클래스 변수 선언 및 초기화
        
    def degree(self):
        return len(self.coef)-1
    
    def display(self, msg="f(x) = "):
        
        
    def add(self, b):
        
        
    def eval(self, x):


    def sub(self, c):
        #
        
    def mult(self, d):
        #
        
        
    def read(Self):
        deg = int(input("다항식의 최고 차수를 입력하시오 : "))
        for n in range(deg+1):
            coef = float(input(		:\tx^%d의 계수 : " %(deg-n)))
            self.coef.append(coef)
        sel.coef.reverse()
        
        
a=Polynomial()
b=Polynomial()
a.read2()
b.read2()
c=a.add(b)
d=a.sub(b)
e=a.mult(b)
f=a-b
a.display("A(x) = ")
b.display("B(x) = ")
c.display("A+B = ")
d.display("A-B = ")
e.display("A*B = ")
f.display("A-B = ")
print("		B(2) = ", b.eval(2))