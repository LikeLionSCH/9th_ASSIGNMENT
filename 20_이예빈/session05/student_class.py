# 학생 정보 관리 프로그램
# 학생 정보를 담은 Student 클래스
# 단! 무조건 '입력'을 받아서 정보들을 저장할 수 있는 형태 ( + 나중에... 미리 입력된 정보 바탕으로 정보 저장하기 / 값 수정하기)
# 생성되는 Student 객체들은 StudentList 에 리스트로 나열하여 저장

# Student 클래스의 필드: name, birth, age, gender, grade
# Student 클래스의 메소드: __init__ setInit, getAvg, getName, printStud 

class Student:

    # ----- 생성자 -----
    def __init__(self):
        self.name=""
        self.birth=""
        self.age=""
        self.gender=""
        self.grade={'kor':0, 'eng':0, 'math':0}
        self.avg=0
        #print(grade)
    
    # ----- 값 입력받아 저장 -----
    def setInit(self):
        print("<학생 정보 입력>")
        self.name=input("이름 입력 : ")
        self.birth=input("생년월일 입력 : ")
        self.age=input("나이 입력 : ")
        self.gender=input("성별 입력 : ")
        print("<학생 성적 입력>")
        self.grade['kor']=int(input("국어 점수 입력 : "))
        self.grade['eng']=int(input("영어 점수 입력 : "))
        self.grade['math']=int(input("수학 점수 입력 : "))

    # ----- 학생의 성적 평균 구하기 -----
    def getAvg(self):
        self.avg=(self.grade['kor']+self.grade['eng']+self.grade['math'])/3
        return self.avg

    # ----- 학생 이름 리턴 -----
    def getName(self):
        return self.name

    # ----- 학생 정보 출력 -----
    def printStud(self):
        print()
        print(f'----------------------- {self.name} 의 정보 ----------------------- ')
        print(f'나이: {self.birth}')
        print(f'생년월일: {self.birth}')
        print(f'성별 : {self.gender}')
        print(f"성적 : 국어 {self.grade['kor']} / 영어 {self.grade['eng']} / 수학 {self.grade['math']}")

# ----- 학생들 정보 담을 빈 StudentList 리스트 생성 -----
StudentList=list()

# ------ 메뉴 입력 받아 학생 객체를 다루는 프로그램 ------
while True:
    print()
    n=int(input("1. 학생 추가, 2. 학생 평균 찾기, 3. 전체 출력, 4. 종료 >> "))
    if n==4:
        break
    
    if n==1:
        s=Student()
        s.setInit()
        StudentList.append(s)
    
    elif n==2:
        sName=input("학생 이름 입력 : ")
        for StudName in StudentList:
            if StudName.getName()==sName:
                print(StudName.getName(), "의 성적 평균 : ", StudName.getAvg())
                break
            print(sName, "발견 실패")
    
    elif n==3:
        for s in StudentList:
            s.printStud()