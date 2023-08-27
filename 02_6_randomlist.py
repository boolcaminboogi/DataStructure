import random

rand_num=[]

for i in range(10):		#10번 랜덤 숫자 뽑기
    a = random.randint(1,100)		#1~100사이의 랜덤 숫자
    rand_num.insert(0, a)		#리스트 0번째에 추가

sum_rand=sum(rand_num)		#리스트 숫자 전체 합

print('생성된 리스트 : ', rand_num)	#리스트 요소 출력
print('리스트의 모든 값들의 합 : ', sum_rand)	#리스트 전체 합 출력
