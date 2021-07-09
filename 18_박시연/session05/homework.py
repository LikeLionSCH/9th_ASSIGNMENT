class Cat:

    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed

    def introduce(self):
        print("제 고양이 " + self.name + "(이)는 " + self.gender + "이고, " + self.breed + "종입니다.")

    def nyang(self):
        print("냐웅")

myCat = Cat("냥구", "암컷", "노르웨이 숲")
myCat.introduce()
myCat.nyang()