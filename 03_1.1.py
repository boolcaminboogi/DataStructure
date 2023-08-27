class Polynominal:
    def_init_(self):
        self.coef=[]
        
    def degree(self):
        return len(self.coef)-1
    
    def display(self, msg="f(x)="):
        #
    
    def add(self, b):
        #
        
    def eval(self, x):
        #
        
    def mi(self, c):
        #
        
    def gob(self, d):
        #
        
    
def read_poly():
    p=Plynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    for n in range(deg+1):
        coef = float(input("\t^%d의 계수 : " %(deg-n)))
        p.coef.append(coef)
    p.coef.reverse()
    return p

#테스트 코드.... 뺄셈, 곱셈 추가
a=read_poly()
b=read_poly()
c=a,add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print("C(2) = ", c.eval(2))