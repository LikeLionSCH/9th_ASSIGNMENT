#Class만들기
#생성자 사용
#필드 2개 이상
#메서드 2개 이상 내장함수 1개 이상 사용

class Cafe:
    def __init__(self):
        print("주문하시겠습니까?")

    def Mydrink(dirnk):
        Cafe.drink = drink 
        print("음료는"+drink+"마실게요")
     
    def Mydesert(desert):
        Cafe.desert = desert
        print("디저트는"+desert+"주세요")

    def Serve(self, drink, desert):
        Cafe.drink = drink
        Cafe.desert = desert
        print("주문하신 "+drink+" 와/과 "+desert+" 나왔습니다")

order = Cafe()
drink = input()
desert = input()
order.Serve(drink,desert)
