#피보나치 수열
import time

#Slow 순환
start_1 = time.time()				#현재 시간 = 시작시간

def fib(n):						#순환으로 구현한 피보나치 수열
        if n==0: return 0 #return 0				#종료조건
        elif n==1: return 1 #return 1				#종료조건
        else:
         return fib(n-1)+fib(n-2) #return fib(n-1)+fib(n-2)		#순환호출
        #print(fib(n))
        
end_1 = time.time()    			#현재 시간 = 종료시간
timer_1 = end_1 - start_1			#총 시간

    
#Fast 반복
start_2 = time.time()

def fib_iter(n):				#반복으로 구현한 피보나치 수열
    
    if(n<2): return n
    
    last =0						#시작 1번째 -> 마지막 값
    current =1					#1 2번째 -> 현재값
    
    for i in range(2, n+1):		#반복루프 2~n까지 n-2번 반복	/ tmp->curr->last순서로 반복
        tmp=current				#tmp에 현재값 대입
        current +=last			#현재값과 마지막 값을 더하고 그를 현재값에 대입
        last = tmp				#마지막 값에 현재값 대입
        #print('n={} 일때 '.format(i+1), current)
    return current

end_2 = time.time()    
timer_2 = end_2-start_2

#결과
print('순환 결과 : ', fib(10))
print("순환 실행시간 = ", timer_1)

print('반복 결과 : ',fib_iter(10))
print("반복 실행시간 = ", timer_2)