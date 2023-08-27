#bag=[]		#bag 클래스 생성방법?

class bag:
    bag=[]
    
    def put(self,item) :
       self.bag.append(item)
    def get_out(self,item):
       self.bag.remove(item)
    
myBag = bag()
myBag.put('휴대폰')
myBag.put('지갑')
myBag.put('손수건')
myBag.put('빗')
myBag.put('자료구조')
myBag.put('야구공')
myBag.put('거울')
print('내 가방 속의 물건 :', myBag.bag)

myBag.put('빗')
myBag.get_out('손수건')
print('내 가방 속의 물건 :', myBag.bag)
