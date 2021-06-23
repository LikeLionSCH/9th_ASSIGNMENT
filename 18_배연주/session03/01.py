# 사용자로부터 숫자 n을 입력받아 n!을 출력하는 프로그램을 작성하라.
# n! = n x (n-1) x (n-2) x ... x 2 x 1
# 0! = 1
n = int(input("숫자를 입력하세요 >> "))

print('{}! ='.format(n), end=' ')

for i in range(n):
    if i == (n-1):
        print('{} = '.format(n-i), end='')
    else:
        print('{}x'.format(n-i), end='')

num = 1
for i in range(1, n+1):
    num *= i
print(num)