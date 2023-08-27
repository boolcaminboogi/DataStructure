pay = int(input("연봉을 입력하세요 : "))
all=pay
tax=0

if pay>15000:		#연봉 15000초과 시 
    tax+=(pay-15000)*0.38
    pay=15000
if pay>8800:		#연봉 8800초과 시
    tax+=(pay-8800)*0.36
    pay=8800
if pay>4600:		#연봉 4600초과 시
    tax+=(pay-4600)*0.24
    pay=4600
if pay>1200:		#연봉1200초과 시
    tax+=(pay-1200)*0.15
    pay=1200
    
tax+=pay*0.06		#연봉 1200이하 시


rest = all-tax		#순수 소득=연봉-세금

print("전제 세금 = ", tax)
print("순수소득 = ", rest)

     
