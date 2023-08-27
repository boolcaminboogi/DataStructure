#bag=[]		#bag 클래스 생성방법?
#bag=[]
class bag:		#bag 클래스 생성
    def insert(self, item) :		#item 삽입함수
       self.bag.insert(item)
    def remove(self, item):		#item 제거 함수
       self.bag.remove(item)
    
myBag = bag()	#bag 클래스
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
myBag.insert('거울')
print('내 가방 속의 물건 :', myBag.bag)

myBag.insert('빗')
myBag.remove('손수건')
print('내 가방 속의 물건 :', myBag.bag)
