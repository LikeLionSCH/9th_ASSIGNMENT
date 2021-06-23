from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json
from requests.api import get
from tabulate import tabulate

# 프로그램 설명 
print("이 프로그램은 예측진료정보를 조회하는 프로그램입니다. ")

#serviceKey 들어있는 json파일 열기
with open("serviceKey.json") as f:
     secret = json.loads(f.read())

# 질병코드
disscode = [[1,"감기"], [2,"눈병"], [3,"식중독"], [4,"천식"], [5,"피부염"]]
# 지역 코드
localcode = [[11,"서울"], [26,"부산"], [27,"대구"],[28,"인천"],[30,"대전"],
[31,"울산"],[41,"경기"],[42,"강원"],[43,"충북"],[44,"충남"],[45,"전북"],
[46,"전남"],[47,"경북"],[48,"경남"],[49,"제주"],[99,"전국"]]
# 질병코드 및 지역코드 출력
print(tabulate(disscode,  headers = ["질병코드","질병명"]))
# 질병코드 입력 
diss = input("질병코드를 입력하세요. ex)1-감기, 2-눈병: ")
print(tabulate(localcode,  headers = ["지역코드","지역명"]))
# 지역코드 입력
local = input("지역코드를 입력하세요. ex_11-서울: ")

# api 호출 
url = 'http://apis.data.go.kr/B550928/dissForecastInfoSvc/getDissForecastInfo'

# 전송할 파라미터 입력 
queryParams = '?' + urlencode(
     { 
     quote_plus('serviceKey'): secret['serviceKey'],
     quote_plus('numOfRows'): '10',
     quote_plus('pageNo'): '1', 
     quote_plus('type'): 'json',  
     quote_plus('dissCd'): diss, 
     quote_plus('znCd'): local
     }
     )

# response 를 get 형식으로 받아서 저장 
# unquote : 한글로 보내준 url 풀어줌
get_data = requests.get(url + unquote(queryParams))
#print(get_data.text)
# 응답 확인(200이면 정상)
print(get_data.status_code)
# json 형식을 딕셔너리 형태로 저장 
res = get_data.json()
#응답메세지를 받기 위한 items생성
items = res['response']['body']['items']

# 질병 예측 진료 건수 출력
print("질병 예측 진료 건수: ", items[0]['cnt'])
# 질병위험도 등급 코드
risk = [[1,'관심'],[2,'주의'],[3,'경고'],[4,'위험']]
print(tabulate(risk,  headers = ["위험도","위험도명"]))
# 위험도 출력
print("위험도는: ", items[0]['risk'])
# 질병 위험도 지침 출력
print("질병 위험도 지침: ",items[0]['dissRiskXpln'])
