class Schedule:
    def __init__(self):
        self.__day = ""
        self.__title = ""
        self.__start = 0

    @property
    def day(self):
        return self.__day

    @property
    def title(self):
        return self.__title

    @property
    def start(self):
        return self.__start

    @day.setter
    def day(self, day):
        self.__day = day

    @title.setter
    def title(self, title):
        self.__title = title

    @start.setter
    def start(self, start):
        self.__start = start

    def showSchedule(self):
        print(f'{self.__day}요일 일정 : {self.__start}시에 {self.__title}')


PS = Schedule()
PS.day = "화"
PS.title = "알고리즘 스터디"
PS.start = 22
PS.showSchedule()

Lion = Schedule()
Lion.day = "수"
Lion.title = "멋사 세션"
Lion.start = 19
Lion.showSchedule()

PS.start = 2
PS.showSchedule() 