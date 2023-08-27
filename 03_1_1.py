class Polynomial:
    def __init__(self):
        self.coef=[]
        
    def degree(Self):
        return len(self.coef)-1
    
    def display(self, msg="f(x) = "):
        
        
    def add(self, b):
        
        
    def eval(self, x):
        for i in range(coef)
            i+=coef[i]*x**(deg-i)
        
    def sub(self, c):
        #
        
    def mult(self, d):
        #
        
        
        
def read_poly():
    p=Polynomial()
    deg=int(input("다항식의 최고차수를 입력하시오 : "))
    for n in range(deg+1):
        coef = float(input(		"\tx^%d의 계수 : " %(deg-n)))
        p.coef.append(coef)
    p.coef.reverse()
    return p

a=read_poly()
b=read_poly()
c=a.add(b)
d=a.sub(b)
e=a.mult(b)
a.display("A(x)= ")
b.display("B(x)= ")
c.display("C(x)= ")
print("C(2) = ", c.eval(2))