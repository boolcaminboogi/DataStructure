import random
answer = random.randint(1,99)
i=1		#시도 횟수
n=10	#시도가능 횟수
#answer = getpass('정답은 : ') #비밀번호처럼 *로 표시하는 방법

while i<=n:
    guess = int(input('두 자리 수 입력 : '))		#예상 숫자
    i+=1	#시도횟수 증가
    if(guess==answer):
        print('정답입니다! 시도 횟수는 %d회 입니다.' %(i-1))		#정답, 시도 횟수
        break		#게임 끝
    elif(guess>answer):		#예상 숫자가 답보다 클 경우
        print('더 작은 숫자 입니다.')
        #max=guess
    elif(guess<answer):		#예상 숫자가 답보다 작을 경우
        print('더 큰 숫자 입니다')
        #min=guess
if i>n:						#시도 횟수가 10회가넘을 경우 게임오
    print('패배. 게임 종료. 정답은 %d입니다' %answer)