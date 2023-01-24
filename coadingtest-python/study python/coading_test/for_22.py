#자연수가 입력으로 주어진다. 이 수의 약수를 출력하고 , 다음 줄에는 약수의 개수 , 다음 줄에는 약수의 총합 , 다음 줄에는 약수의 곱의 일의 자리수를 출력한다.
a = int(input())

result_1 = ""
result_2 = 0
result_3 = 0
result_4 = 1

for i in range(1,a+1,1):
    if ((a%i) == 0):
        result_1 += str(i)
        if i == a:
            pass
        else:
            result_1 += " "
        result_2 +=1
        result_3 +=i
        result_4 *=i

print(result_1)
print(result_2)
print(result_3)
result_4 = list(str(result_4))
print(result_4[len(result_4)-1])
