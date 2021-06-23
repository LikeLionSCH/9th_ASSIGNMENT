lst = [[0 for col in range(5)] for row in range(5)]
selectedLst = [0, 0]   # 출력을 위한 임시 리스트
element = 0     # 리스트 요소를 위한 변수

# lst 리스트에 0~25 요소 추가
for lineCount in range(5):
    for elementCount in range(5):
        lst[lineCount][elementCount] = element
        element += 1

# selected 리스트에 2, 4번째 요소 추가 후 출력
for lineCount in range(5):
    selectedLst[0] = lst[lineCount][1]
    selectedLst[1] = lst[lineCount][3]
    print(selectedLst)