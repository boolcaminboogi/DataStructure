#추상자료형

def contains(bag, item):		#bag에 항목 item이 있는지 검사
    return item in bag			#in 연산자 사용

def insert(bag, item):			#bag에 항목 item을 추가
    bag.append(item)			#append 메소드 사용
            
def remove(bag, item):			#bag에서 항목 item을 삭제
    bag.remove(item)			#remove 메소드 사용

def count(bag):					#bag 안의 전체 항목 개수를 계산
    return len(bag)				#len 함수 사용

def num0f(bag,item):			#bag에 들어있는 item 개수 계산
    count = 0					#item의 개수를 세기 위한 변수
    for i in bag:
        if i==item:
            count += 1			#bag에 item이 있을 경우 개수 하나 증가
    return count				#item 개수 반환

myBag =[]						#bag를 위한 빈 리스트

insert(myBag, '휴대폰')			#item 추가
insert(myBag, '지갑')
insert(myBag, '손수건')
insert(myBag, '빗')
insert(myBag, '자료구조')
insert(myBag, '야구공')
insert(myBag, '거울')

print('내 가방속의 물건 : ', myBag)
#print('최초 휴대폰의 개수 : ', num0f(myBag,'휴대폰'))
#print('최초 빗의 개수 : ', num0f(myBag,'빗'))

insert(myBag, '빗')			#item 휴대폰 추가
remove(myBag, '손수건')				#item 빗 삭제

print('내 가방속의 물건 : ', myBag)
#print('현재 휴대폰의 개수 : ', num0f(myBag,'휴대폰'))
#print('현재 빗의 개수 : ', num0f(myBag,'빗'))


