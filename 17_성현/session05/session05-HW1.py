class intro:
    favoriteThings = ['코딩', '게임']
    global name 
    def __init__(self):
        print('아이엠 그라운드 자기소개 하기 !')

    def myName (UserNm) :
        intro.name = UserNm
        print('내 이름은 ', intro.name,'이야.')
    
    def favorite(things) : 
        intro.favoriteThings.append(things)
        print('내가 좋아하는 것은 ',intro.favoriteThings,'이야! 같이 할래??')
    
    def ImGround(self, UserNm, things):
        intro.myName(UserNm)
        intro.favorite(things)

selfIntro = intro()
myNm = input()
myFavorite = input()
selfIntro.ImGround(myNm,myFavorite)