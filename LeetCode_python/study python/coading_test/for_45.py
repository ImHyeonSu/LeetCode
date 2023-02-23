a = int(input())
result = a
result_i = 0
counter = 0
for i in range(1,a,2):
    if (result % 2) == 1:
        result_i = a/result
        result_i = int(result_i)
    else:
        result //= 2
if result_i == 0:
    result_i = a / result
    result_i = int(result_i)
while result_i >= 2:
    result_i /=2
    counter +=1

print(result,counter)
# 프로그램 명: tf
# 제한시간: 1 초
# 양의 정수 n 을 입력으로 받아 n = o * 2^p 가 되는 홀수 o 와 정수 p 를 구하는 것이 문제이다.
#
# 예를 들어 24 를 입력으로 받으면 o = 3 , p = 3 이다.
#
# 입력
# 정수 n 이 입력으로 주어진다. ( 1 <= n <= 10^6 )
# 출력
# 한 줄에 o 와 p 를 출력한다.
# 입출력 예
# 입력
#
# 24
#
# 출력
#
# 3 3
# 출처: Central European Programming Contest