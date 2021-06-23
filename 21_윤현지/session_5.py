class Nct:
    #생성자
    def __init__(self, name, team, age):
        #필드
        self.name = name
        self.team = team
        self.age = age
    #매서드
    def Nameteam(self):
        print("그 잘생긴 분의 이름은 "+self.name+"이고, NCT 중 소속된 팀은"+self.team+"임")

    def Age(self):
        print("참고로 나이는"+self.age+"살이야.")

jm = Nct("나재민", "dream", "22")
dh = Nct("이동혁", "dream", "22")
jh = Nct("정재현", "127", "25")

#출력
print("응? 저 분 누구냐고?")
jm.Nameteam()
jm.Age()

print("응? 저 분은 누구냐고?")
dh.Nameteam()
dh.Age()

print("마지막으로 저 분은 누구냐고?")
jh.Nameteam()
jh.Age()
print("잘생겼지? 하하")