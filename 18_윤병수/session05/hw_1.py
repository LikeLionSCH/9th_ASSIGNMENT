#class 만들기
class Customer :
    # ----- 구매 목록 리스트 생성 -----
    items = []

    # ----- 생성자 -----
    def __init__ (self, points=0):
        self.name = input("이름 입력 : ")
        self.age = input("나이 입력 : ")
        self.sex = input("성별 입력 : ")
        self.live = input("거주 지역 입력 : ")
        self.number = input("전화번호 입력 : ")
        self.points = 0

    # ----- 입력 받아 고객 정보 입력 -----
    def updateInfo(self) :
        print("-- 고객 정보 변경 --")
        self.live = input("거주 지역 변경 : ")
        self.number = input("전화번호 변경 : ")

    # ----- 고객 개인정보 출력 -----
    def getInfo(self) :
        print("--", self.name, "고객님의 정보 출력--")
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'성별 : {self.sex}')
        print(f'전화번호 : {self.number}')

    # ----- 고객 개인정보 개별 항목 리턴 -----
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex

    def getLive(self):
        return self.live

    def getNumber(self):
        return self.number

    # ----- 구매 목록 입력 후 리스트에 추가 -----
    def addItem(self, item) :
        print("-- 구매 목록 입력 --")
        self.items.append(item)
        print(item, "을(를) 구매했습니다.")

    # ----- 구매 목록 리스트 출력 -----
    def getItem(self) :
        print("-- 구매 목록 출력 --")
        print("현재까지", self.items, "을(를) 구매했습니다.")

    # ----- 구매 금액에 따른 포인트 적립 -----
    # ----- 포인트 변수 선언 -----
    def addPoint(self, price) :
        val = int(price * 0.1)
        print("고객님의 기존 포인트는 {0} 점이며, 이번에 {1} 점이 추가되었습니다." .format(self.points, price*0.1))
        self.points += val
        return self.points

    def getPoint(self) :
        print("최종 적립 포인트는 {0} 점 입니다." .format(self.points))

hyb = Customer()
print(hyb.name, hyb.age, hyb.sex, hyb.live, hyb.number)
hyb.getInfo()
hyb.updateInfo()
hyb.addItem("pepsi-zero")
hyb.addItem("chocolate")
hyb.getItem()
hyb.addPoint(1000)
hyb.addPoint(2000)
hyb.getPoint()